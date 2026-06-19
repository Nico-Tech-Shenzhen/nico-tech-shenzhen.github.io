#!/usr/bin/env python3
from __future__ import annotations

import argparse
import email.utils
import hashlib
import html
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlparse
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "tools" / "activity_sources.example.json"
DEFAULT_REPORT = ROOT / "reports" / "external-activity-audit.md"

SUPPORTED_PLATFORMS = {"youtube", "podcast", "medium", "note"}
PLACEHOLDER_VALUES = {"", "todo", "tbd", "placeholder", "example"}


@dataclass
class SourceResult:
    source: dict[str, Any]
    status: str
    items: list[dict[str, Any]] = field(default_factory=list)
    issues: list[str] = field(default_factory=list)


def is_placeholder_url(value: str) -> bool:
    value = (value or "").strip()
    if not value:
        return True
    lowered = value.lower()
    if lowered in PLACEHOLDER_VALUES:
        return True
    if "example.com" in lowered:
        return True
    if lowered.startswith("<") and lowered.endswith(">"):
        return True
    if "channel_id_here" in lowered or "feed_url_here" in lowered:
        return True
    return False


def normalize_url(url: str) -> str:
    url = (url or "").strip()
    if not url:
        return ""
    parsed = urlparse(url)
    cleaned = parsed._replace(query="", fragment="")
    return cleaned.geturl().rstrip("/")


def text_of(element: ET.Element | None) -> str:
    if element is None or element.text is None:
        return ""
    return html.unescape(element.text).strip()


def strip_html(value: str, limit: int = 280) -> str:
    value = html.unescape(value or "")
    value = re.sub(r"<script\b.*?</script>", "", value, flags=re.I | re.S)
    value = re.sub(r"<style\b.*?</style>", "", value, flags=re.I | re.S)
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    if len(value) > limit:
        return value[: limit - 1].rstrip() + "..."
    return value


def parse_date(value: str) -> str:
    value = (value or "").strip()
    if not value:
        return ""
    try:
        parsed = email.utils.parsedate_to_datetime(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.isoformat()
    except Exception:
        pass
    try:
        normalized = value.replace("Z", "+00:00")
        return datetime.fromisoformat(normalized).isoformat()
    except Exception:
        return value


def fetch_text(url: str, timeout: int = 30) -> str:
    req = Request(
        url,
        headers={
            "User-Agent": "NicoTechShenzhenActivityAudit/0.1",
            "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml;q=0.9, */*;q=0.5",
        },
    )
    with urlopen(req, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def first_child(element: ET.Element, names: tuple[str, ...]) -> ET.Element | None:
    for child in list(element):
        local = child.tag.rsplit("}", 1)[-1].lower()
        if local in names:
            return child
    return None


def all_children(element: ET.Element, name: str) -> list[ET.Element]:
    return [child for child in list(element) if child.tag.rsplit("}", 1)[-1].lower() == name]


def atom_link(entry: ET.Element) -> str:
    fallback = ""
    for link in all_children(entry, "link"):
        href = (link.attrib.get("href") or "").strip()
        rel = (link.attrib.get("rel") or "alternate").strip()
        if href and rel == "alternate":
            return href
        if href and not fallback:
            fallback = href
    return fallback


def parse_feed(xml_text: str) -> tuple[list[dict[str, str]], list[str]]:
    issues: list[str] = []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as exc:
        return [], [f"XML parse error: {exc}"]

    root_name = root.tag.rsplit("}", 1)[-1].lower()
    entries: list[dict[str, str]] = []

    if root_name == "rss" or root.find("channel") is not None:
        channel = root.find("channel")
        if channel is None:
            issues.append("RSS channel element not found.")
            return entries, issues
        for item in channel.findall("item"):
            content = first_child(item, ("encoded",))
            description = first_child(item, ("description", "summary"))
            entries.append(
                {
                    "title": text_of(first_child(item, ("title",))),
                    "link": text_of(first_child(item, ("link",))),
                    "guid": text_of(first_child(item, ("guid",))),
                    "date": parse_date(text_of(first_child(item, ("pubdate", "published", "updated")))),
                    "summary": strip_html(text_of(content) or text_of(description)),
                    "image": image_from_rss_item(item),
                }
            )
        return entries, issues

    if root_name == "feed":
        for entry in all_children(root, "entry"):
            summary = first_child(entry, ("summary", "content"))
            entries.append(
                {
                    "title": text_of(first_child(entry, ("title",))),
                    "link": atom_link(entry),
                    "guid": text_of(first_child(entry, ("id",))),
                    "date": parse_date(text_of(first_child(entry, ("published", "updated")))),
                    "summary": strip_html(text_of(summary)),
                    "image": image_from_atom_entry(entry),
                }
            )
        return entries, issues

    issues.append(f"Unsupported feed root: {root.tag}")
    return entries, issues


def image_from_rss_item(item: ET.Element) -> str:
    for child in list(item):
        local = child.tag.rsplit("}", 1)[-1].lower()
        if local in {"thumbnail", "content"}:
            url = (child.attrib.get("url") or "").strip()
            medium = (child.attrib.get("medium") or "").strip()
            if url and (local == "thumbnail" or medium == "image"):
                return url
        if local == "enclosure":
            url = (child.attrib.get("url") or "").strip()
            mime = (child.attrib.get("type") or "").strip()
            if url and mime.startswith("image/"):
                return url
    return ""


def image_from_atom_entry(entry: ET.Element) -> str:
    for link in all_children(entry, "link"):
        href = (link.attrib.get("href") or "").strip()
        rel = (link.attrib.get("rel") or "").strip()
        mime = (link.attrib.get("type") or "").strip()
        if href and (rel in {"enclosure", "thumbnail"} or mime.startswith("image/")):
            return href
    return ""


def external_id_for(source: dict[str, Any], entry: dict[str, str]) -> str:
    platform = source.get("source_platform", "")
    source_id = source.get("id", "")
    guid = entry.get("guid", "")
    link = entry.get("link", "")

    if platform == "youtube":
        video_id = youtube_video_id(guid) or youtube_video_id(link)
        if video_id:
            return video_id

    if platform == "medium":
        medium_id = medium_post_id(guid) or medium_post_id(link)
        if medium_id:
            return medium_id

    if platform == "note":
        note_id = note_entry_id(guid) or note_entry_id(link)
        if note_id:
            return note_id

    if guid:
        return guid
    if link:
        return stable_hash(normalize_url(link))
    return stable_hash(f"{source_id}:{entry.get('title', '')}:{entry.get('date', '')}")


def normalized_id_for(source: dict[str, Any], external_id: str) -> str:
    platform = source.get("source_platform", "")
    source_id = source.get("id", "")
    if source_id == "youtube_ja":
        return f"youtube:ja:{external_id}"
    if source_id == "youtube_en":
        return f"youtube:en:{external_id}"
    return f"{platform}:{external_id}"


def youtube_video_id(value: str) -> str:
    value = value or ""
    if "yt:video:" in value:
        return value.rsplit(":", 1)[-1].strip()
    parsed = urlparse(value)
    query = parse_qs(parsed.query)
    if "v" in query and query["v"]:
        return query["v"][0]
    match = re.search(r"/(?:shorts|embed)/([A-Za-z0-9_-]{6,})", parsed.path)
    if match:
        return match.group(1)
    if "youtu.be" in parsed.netloc:
        candidate = parsed.path.strip("/")
        if candidate:
            return candidate
    return ""


def medium_post_id(value: str) -> str:
    match = re.search(r"(?:/p/|-)([0-9a-f]{6,})(?:[/?#]|$)", value or "")
    return match.group(1) if match else ""


def note_entry_id(value: str) -> str:
    match = re.search(r"/n/([A-Za-z0-9_-]+)", value or "")
    return match.group(1) if match else ""


def stable_hash(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:16]


def normalize_entry(source: dict[str, Any], entry: dict[str, str], imported_at: str) -> dict[str, Any]:
    external_id = external_id_for(source, entry)
    return {
        "id": normalized_id_for(source, external_id),
        "activity_type": source.get("activity_type", "external"),
        "source_platform": source.get("source_platform", ""),
        "title": entry.get("title", ""),
        "date": entry.get("date", ""),
        "source_url": normalize_url(entry.get("link", "")),
        "canonical_url": "",
        "summary": entry.get("summary", ""),
        "image": entry.get("image", ""),
        "language": source.get("language", "ja"),
        "topics": [],
        "featured": False,
        "source_id": source.get("id", ""),
        "external_id": external_id,
        "imported_at": imported_at,
    }


def audit_source(source: dict[str, Any], imported_at: str) -> SourceResult:
    source_id = source.get("id", "(missing)")
    platform = source.get("source_platform", "")
    feed_url = source.get("feed_url", "")
    issues: list[str] = []

    if not source.get("enabled", True):
        return SourceResult(source, "disabled", issues=["Source is disabled."])
    if platform not in SUPPORTED_PLATFORMS:
        return SourceResult(source, "skipped", issues=[f"Unsupported platform: {platform}"])
    if is_placeholder_url(feed_url):
        return SourceResult(source, "skipped", issues=["No real feed_url configured yet."])

    try:
        xml_text = fetch_text(feed_url)
    except HTTPError as exc:
        return SourceResult(source, "failed", issues=[f"HTTP error for {source_id}: {exc.code} {exc.reason}"])
    except URLError as exc:
        return SourceResult(source, "failed", issues=[f"URL error for {source_id}: {exc.reason}"])
    except Exception as exc:
        return SourceResult(source, "failed", issues=[f"Fetch error for {source_id}: {exc}"])

    parsed_items, parse_issues = parse_feed(xml_text)
    issues.extend(parse_issues)
    normalized = [normalize_entry(source, item, imported_at) for item in parsed_items]
    return SourceResult(source, "tested", normalized, issues)


def find_duplicates(results: list[SourceResult]) -> list[str]:
    seen_ids: dict[str, str] = {}
    seen_urls: dict[str, str] = {}
    warnings: list[str] = []

    for result in results:
        for item in result.items:
            item_id = item["id"]
            url = item["source_url"]
            source_id = item["source_id"]
            if item_id in seen_ids:
                warnings.append(f"Duplicate normalized ID `{item_id}` in `{seen_ids[item_id]}` and `{source_id}`.")
            else:
                seen_ids[item_id] = source_id
            if url:
                if url in seen_urls:
                    warnings.append(f"Duplicate source URL `{url}` in `{seen_urls[url]}` and `{source_id}`.")
                else:
                    seen_urls[url] = source_id
    return warnings


def md_escape(value: Any) -> str:
    text = str(value if value is not None else "")
    return text.replace("|", "\\|").replace("\n", " ")


def write_report(path: Path, config_path: Path, results: list[SourceResult], duplicate_warnings: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append("# External Activity Feed Audit")
    lines.append("")
    lines.append(f"Generated: `{datetime.now(timezone.utc).isoformat()}`")
    lines.append("")
    lines.append("This is a read-only prototype audit. It normalizes feed entries in memory and does not write `data/activity/*.json`, Markdown posts, `public/`, templates, config, navigation, or homepage files.")
    lines.append("")
    lines.append("## Source Config Format")
    lines.append("")
    lines.append(f"Config file: `{config_path.relative_to(ROOT)}`")
    lines.append("")
    lines.append("Each source has:")
    lines.append("")
    lines.append("- `id`: stable source ID, for example `youtube_ja` or `youtube_en`")
    lines.append("- `label`: human-readable source name")
    lines.append("- `source_platform`: `youtube`, `podcast`, `medium`, or `note`")
    lines.append("- `activity_type`: `video`, `podcast`, or `external`")
    lines.append("- `language`: default language for items from this source")
    lines.append("- `feed_url`: RSS/Atom feed URL")
    lines.append("- `site_url`: public profile/channel URL")
    lines.append("- `enabled`: whether the source should be tested")
    lines.append("")
    lines.append("YouTube sources are intentionally separate: `youtube_ja` uses IDs like `youtube:ja:VIDEO_ID`; `youtube_en` uses IDs like `youtube:en:VIDEO_ID`.")
    lines.append("")
    lines.append("## Sources Tested")
    lines.append("")
    lines.append("| source_id | platform | activity_type | language | status | items | issues |")
    lines.append("| --- | --- | --- | --- | --- | ---: | --- |")
    for result in results:
        source = result.source
        lines.append(
            "| "
            + " | ".join(
                [
                    md_escape(source.get("id", "")),
                    md_escape(source.get("source_platform", "")),
                    md_escape(source.get("activity_type", "")),
                    md_escape(source.get("language", "")),
                    md_escape(result.status),
                    str(len(result.items)),
                    md_escape("; ".join(result.issues)),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append("## Sample Normalized Items")
    lines.append("")
    for result in results:
        source_id = result.source.get("id", "")
        lines.append(f"### {source_id}")
        lines.append("")
        if not result.items:
            lines.append("_No items normalized._")
            lines.append("")
            continue
        lines.append("| id | date | title | source_url | language |")
        lines.append("| --- | --- | --- | --- | --- |")
        for item in result.items[:5]:
            lines.append(
                "| "
                + " | ".join(
                    [
                        md_escape(item["id"]),
                        md_escape(item["date"]),
                        md_escape(item["title"]),
                        md_escape(item["source_url"]),
                        md_escape(item["language"]),
                    ]
                )
                + " |"
            )
        lines.append("")
    lines.append("## Duplicate Warnings")
    lines.append("")
    if duplicate_warnings:
        for warning in duplicate_warnings:
            lines.append(f"- {warning}")
    else:
        lines.append("- No duplicate normalized IDs or source URLs found among normalized items.")
    lines.append("")
    lines.append("## Parsing Issues")
    lines.append("")
    any_issue = False
    for result in results:
        for issue in result.issues:
            any_issue = True
            lines.append(f"- `{result.source.get('id', '')}`: {issue}")
    if not any_issue:
        lines.append("- No parsing issues reported.")
    lines.append("")
    lines.append("## Recommended Next Step")
    lines.append("")
    lines.append("Replace placeholder `feed_url` values with real source feeds, then re-run this audit. After the normalized samples look correct, add a dry-run importer that writes proposed `data/activity/*.json` changes to a report before enabling persistent data output.")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def load_config(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    sources = data.get("sources")
    if not isinstance(sources, list):
        raise ValueError("Config must contain a `sources` array.")
    return [source for source in sources if isinstance(source, dict)]


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only audit for external activity feeds.")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    config_path = args.config if args.config.is_absolute() else ROOT / args.config
    report_path = args.report if args.report.is_absolute() else ROOT / args.report

    sources = load_config(config_path)
    imported_at = datetime.now(timezone.utc).isoformat()
    results = [audit_source(source, imported_at) for source in sources]
    duplicate_warnings = find_duplicates(results)
    write_report(report_path, config_path, results, duplicate_warnings)

    tested = sum(1 for result in results if result.status == "tested")
    skipped = sum(1 for result in results if result.status == "skipped")
    failed = sum(1 for result in results if result.status == "failed")
    total_items = sum(len(result.items) for result in results)

    print("External activity feed audit complete.")
    print(f"Sources: {len(results)} total, {tested} tested, {skipped} skipped, {failed} failed.")
    print(f"Normalized items: {total_items}")
    print(f"Duplicate warnings: {len(duplicate_warnings)}")
    print(f"Report: {report_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
