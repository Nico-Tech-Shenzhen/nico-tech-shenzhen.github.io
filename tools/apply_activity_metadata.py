#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONTENT_ROOT = ROOT / "content"
AUDIT_REPORT = ROOT / "reports" / "activity-metadata-audit.md"
DRY_RUN_REPORT = ROOT / "reports" / "activity-metadata-bulk-dry-run.md"

METADATA_FIELDS = [
    "activity_type",
    "source_platform",
    "source_url",
    "language",
    "topics",
    "featured",
]

VALID_ACTIVITY_TYPES = {"post", "monthly_report", "talk", "paper", "book", "video", "podcast", "external"}
VALID_SOURCE_PLATFORMS = {"hugo", "medium", "note", "youtube", "podcast", "fabcross", "conference", "book", "paper"}
VALID_LANGUAGES = {"ja", "en", "mixed"}
KNOWN_SECTIONS = {"archive", "fabcross", "posts", "shenzhen", "teardown"}

TOPIC_RULES = [
    ("shenzhen", ("shenzhen", "深圳", "深セン", "華強北", "huaqiangbei")),
    ("teardown", ("teardown", "分解", "decap", "reverse engineering")),
    ("maker", ("maker", "メイカー", "make:", "make ", "diy", "tinkering")),
    ("maker-faire", ("maker faire", "メイカーフェア", "makerfaire")),
    ("m5stack", ("m5stack", "stackchan", "stamp", "atom", "core2")),
    ("ai", (" ai ", "chatgpt", "openai", "deepseek", "physical ai", "フィジカルai")),
    ("robotics", ("robot", "robotics", "ロボット", "robomaster", "drone", "ドローン", "mycobot")),
    ("open-source", ("open source", "open-source", "オープンソース", "risc-v", "riscv")),
    ("hardware", ("hardware", "ハードウェア", "pcba", "soc", "chip", "半導体", "ic")),
    ("manufacturing", ("manufacturing", "supply chain", "factory", "製造", "工場")),
    ("community", ("community", "コミュニティ", "nico-tech", "ニコ技")),
    ("education", ("education", "stem", "steam", "university", "大学", "講義")),
    ("events", ("event", "events", "meetup", "conference", "tour", "イベント", "ミートアップ", "観察会")),
    ("book", ("book", "書籍", "出版", "深センの歩き方", "メイカーズのエコシステム", "prototype city")),
    ("design", ("design", "デザイン")),
    ("iot", ("iot",)),
    ("risc-v", ("risc-v", "riscv")),
    ("writing", ("writing", "英文", "文章")),
]


@dataclass
class Page:
    path: Path
    rel_path: str
    fm_type: str | None
    fm_body: str
    body: str
    params: dict[str, Any]


@dataclass
class Proposal:
    page: Page
    metadata: dict[str, Any]
    reason: str
    warnings: list[str]


@dataclass
class LanguageSignal:
    language: str
    japanese_chars: int
    english_words: int
    confidence: str
    reason: str


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def split_frontmatter(text: str) -> tuple[str | None, str, str]:
    if text.startswith("---\n") or text.startswith("---\r\n"):
        match = re.match(r"^---[^\S\r\n]*\r?\n(.*?)\r?\n---[^\S\r\n]*\r?\n(.*)$", text, re.S)
        if match:
            return "yaml", match.group(1), match.group(2)
    if text.startswith("+++\n") or text.startswith("+++\r\n"):
        match = re.match(r"^\+\+\+\s*\r?\n(.*?)\r?\n\+\+\+\s*\r?\n(.*)$", text, re.S)
        if match:
            return "toml", match.group(1), match.group(2)
    return None, "", text


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_inline_list(value: str) -> list[str]:
    value = value.strip()
    if not (value.startswith("[") and value.endswith("]")):
        return [strip_quotes(value)] if value else []
    inner = value[1:-1].strip()
    if not inner:
        return []
    parts = re.findall(r'"([^"]*)"|\'([^\']*)\'|([^,\s][^,]*)', inner)
    items = []
    for double, single, bare in parts:
        item = strip_quotes((double or single or bare).strip())
        if item:
            items.append(item)
    return items


def parse_frontmatter(fm_type: str | None, body: str) -> dict[str, Any]:
    if fm_type not in {"yaml", "toml"}:
        return {}

    params: dict[str, Any] = {}
    lines = body.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue

        match = re.match(r"^([A-Za-z0-9_-]+)\s*[:=]\s*(.*)$", line)
        if not match:
            i += 1
            continue

        key, raw_value = match.group(1), match.group(2).strip()
        if fm_type == "yaml" and raw_value == "":
            block_items: list[str] = []
            j = i + 1
            while j < len(lines):
                block_match = re.match(r"^\s+-\s*(.+?)\s*$", lines[j])
                if not block_match:
                    break
                block_items.append(strip_quotes(block_match.group(1)))
                j += 1
            if block_items:
                params[key] = block_items
                i = j
                continue
            params[key] = ""
        elif raw_value.startswith("[") and raw_value.endswith("]"):
            params[key] = parse_inline_list(raw_value)
        else:
            raw_value = re.split(r"\s+#", raw_value, maxsplit=1)[0].strip()
            params[key] = strip_quotes(raw_value)
        i += 1
    return params


def load_page(path: Path) -> Page:
    text = path.read_text(encoding="utf-8")
    fm_type, fm_body, body = split_frontmatter(text)
    return Page(path, rel(path), fm_type, fm_body, body, parse_frontmatter(fm_type, fm_body))


def bool_param(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() == "true"


def detect_section(path: Path) -> str:
    parts = path.relative_to(CONTENT_ROOT).parts
    if len(parts) <= 1:
        return "root"
    first = parts[0]
    if first in KNOWN_SECTIONS:
        return first
    if re.fullmatch(r"\d{4}", first):
        return "year-bundle"
    return first


def normalize_tags(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(v) for v in value]
    if isinstance(value, str) and value:
        return [value]
    return []


def has_any(text: str, needles: tuple[str, ...]) -> bool:
    return any(needle in text for needle in needles)


def has_word(text: str, word: str) -> bool:
    return re.search(rf"(?<![a-z0-9]){re.escape(word)}(?![a-z0-9])", text) is not None


def clean_body_for_language(body: str) -> str:
    text = re.sub(r"```.*?```", " ", body, flags=re.S)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", text)
    text = re.sub(r"\{[^}]*\}", " ", text)
    text = re.sub(r"[-*_#>`~=\[\](){}/\\|:;,.!?0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def detect_language_signal(body: str) -> LanguageSignal:
    text = clean_body_for_language(body)
    japanese_chars = len(re.findall(r"[\u3040-\u30ff\u4e00-\u9fff]", text))
    english_words = len(re.findall(r"\b[A-Za-z][A-Za-z'-]{2,}\b", text))

    if japanese_chars >= 300 and english_words >= 150:
        return LanguageSignal("mixed", japanese_chars, english_words, "high", "substantial Japanese and English body text")
    if japanese_chars >= 120 and japanese_chars >= english_words * 3:
        return LanguageSignal("ja", japanese_chars, english_words, "high", "Japanese body text is clearly dominant")
    if english_words >= 80 and english_words >= max(20, japanese_chars / 2):
        return LanguageSignal("en", japanese_chars, english_words, "high", "English body text is clearly dominant")
    if japanese_chars >= 40 and japanese_chars >= english_words:
        return LanguageSignal("ja", japanese_chars, english_words, "medium", "Japanese body text appears dominant but sample is short")
    if english_words >= 30 and english_words > japanese_chars:
        return LanguageSignal("en", japanese_chars, english_words, "medium", "English body text appears dominant but sample is short")
    return LanguageSignal("mixed", japanese_chars, english_words, "low", "not enough clean body text for confident language detection")


def detect_title_language(title: str) -> str:
    japanese_chars = len(re.findall(r"[\u3040-\u30ff\u4e00-\u9fff]", title))
    english_words = len(re.findall(r"\b[A-Za-z][A-Za-z'-]{2,}\b", title))
    if japanese_chars >= 4 and english_words >= 4:
        return "mixed"
    if japanese_chars >= 4:
        return "ja"
    if english_words >= 4:
        return "en"
    return "unknown"


def detect_activity_type(page: Page, tags: list[str]) -> str:
    title = str(page.params.get("title", ""))
    strong_text = f" {title} {' '.join(tags)} {page.rel_path} ".lower()
    if "monthly-report" in {tag.lower() for tag in tags} or has_any(
        strong_text, ("月次報告", "monthly report", "monthly news", "monthly-report")
    ):
        return "monthly_report"
    if has_any(strong_text, ("podcast", "ポッドキャスト")) and not has_any(strong_text, ("月次報告", "monthly")):
        return "podcast"
    if has_any(strong_text, ("youtube", "youtu.be", " video", " videos", "動画", "映像")):
        return "video"
    if has_word(strong_text, "paper") or has_any(strong_text, ("論文", "research-at-scale", "research at scale")):
        return "paper"
    if has_any(strong_text, ("talk", "presentation", "講演", "登壇", "lecture", "講義")):
        return "talk"
    return "post"


def activity_confidence(page: Page, activity_type: str, tags: list[str]) -> tuple[str, str]:
    title = str(page.params.get("title", ""))
    strong_text = f" {title} {' '.join(tags)} {page.rel_path} ".lower()
    if activity_type == "post":
        return "high", "default article/post classification"
    if activity_type == "monthly_report":
        return "high", "monthly-report tag or title signal"
    if activity_type == "talk" and has_any(strong_text, ("talk", "講演", "登壇", "lecture", "presentation")):
        return "high", "talk/lecture signal in title or path"
    if activity_type == "video" and has_any(strong_text, ("youtube", "youtu.be", "動画", "video")):
        return "high", "video signal in title or path"
    if activity_type == "paper" and has_any(strong_text, ("論文", "paper", "research at scale", "research-at-scale")):
        return "medium", "paper/research signal in title or path"
    if activity_type == "podcast" and has_any(strong_text, ("podcast", "ポッドキャスト")):
        return "medium", "podcast signal in title or path"
    return "low", f"weak signal for {activity_type}"


def detect_source_platform(page: Page, activity_type: str) -> str:
    section = detect_section(page.path)
    source = str(page.params.get("source", "")).lower()
    if activity_type == "talk":
        return "conference"
    if activity_type == "paper":
        return "paper"
    if activity_type == "podcast":
        return "podcast"
    if activity_type == "video":
        return "youtube" if "youtube" in f"{page.rel_path} {page.body[:1000]}".lower() else "medium"
    if "note.com" in source:
        return "note"
    if "medium.com" in source:
        return "medium"
    if section == "fabcross":
        return "fabcross"
    return "medium"


def detect_topics(page: Page, activity_type: str, tags: list[str]) -> list[str]:
    title = str(page.params.get("title", ""))
    section = detect_section(page.path)
    haystack = f" {title} {' '.join(tags)} {section} {page.body[:2000]} ".lower()
    topics = set()
    if section in {"shenzhen", "teardown", "fabcross"}:
        topics.add(section)
    for topic, needles in TOPIC_RULES:
        if has_any(haystack, tuple(needle.lower() for needle in needles)):
            topics.add(topic)

    if activity_type == "monthly_report":
        topics.discard("podcast")
    if activity_type != "podcast" and "podcast" in topics:
        podcast_subject = has_any(f" {title} ".lower(), ("podcast", "ポッドキャスト"))
        if not podcast_subject:
            topics.discard("podcast")

    if "event" in topics:
        topics.remove("event")
        topics.add("events")
    return sorted(topics)


def has_existing_metadata(page: Page) -> bool:
    return any(field in page.params for field in METADATA_FIELDS)


def existing_metadata_valid(page: Page) -> tuple[bool, str]:
    missing = [field for field in METADATA_FIELDS if field not in page.params]
    if missing:
        return False, f"missing metadata fields: {', '.join(missing)}"
    if str(page.params.get("activity_type")) not in VALID_ACTIVITY_TYPES:
        return False, "invalid activity_type"
    if str(page.params.get("source_platform")) not in VALID_SOURCE_PLATFORMS:
        return False, "invalid source_platform"
    if str(page.params.get("language")) not in VALID_LANGUAGES:
        return False, "invalid language"
    topics = page.params.get("topics")
    if not isinstance(topics, list):
        return False, "topics is not a list"
    if "event" in topics:
        return False, "topic uses event instead of events"
    if bool_param(page.params.get("featured")) not in {True, False}:
        return False, "featured is not boolean-like"
    return True, "complete schema"


def audit_manual_reasons(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    reasons: dict[str, str] = {}
    in_manual = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## Files Requiring Manual Review"):
            in_manual = True
            continue
        if in_manual and line.startswith("## "):
            break
        if not in_manual or not line.startswith("| `content/"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) >= 2:
            reasons[parts[0].strip("`")] = parts[1]
    return reasons


def skip_reason(page: Page, manual_reasons: dict[str, str]) -> str | None:
    if page.rel_path in manual_reasons:
        return manual_reasons[page.rel_path]
    if page.rel_path == "content/about.md":
        return "site page"
    if page.path.name == "_index.md":
        return "section/list page"
    if page.fm_type is None:
        return "missing frontmatter"
    if page.fm_type != "yaml":
        return "non-YAML frontmatter"
    if bool_param(page.params.get("draft", False)):
        return "draft"
    if not page.params.get("title"):
        return "missing title"
    if not page.params.get("date"):
        return "missing date"
    return None


def proposed_metadata(page: Page) -> tuple[dict[str, Any], LanguageSignal]:
    tags = normalize_tags(page.params.get("tags"))
    activity_type = detect_activity_type(page, tags)
    language_signal = detect_language_signal(page.body)
    return {
        "activity_type": activity_type,
        "source_platform": detect_source_platform(page, activity_type),
        "source_url": "",
        "language": language_signal.language,
        "topics": detect_topics(page, activity_type, tags),
        "featured": False,
    }, language_signal


def review_reasons(page: Page, metadata: dict[str, Any], language_signal: LanguageSignal) -> list[str]:
    tags = normalize_tags(page.params.get("tags"))
    reasons: list[str] = []
    if language_signal.confidence == "low":
        reasons.append(
            f"language confidence low ({language_signal.japanese_chars} Japanese chars, {language_signal.english_words} English words)"
        )

    title_language = detect_title_language(str(page.params.get("title", "")))
    if title_language in {"ja", "en"} and metadata["language"] in {"ja", "en"} and title_language != metadata["language"]:
        reasons.append(f"title/body language disagree strongly (title={title_language}, body={metadata['language']})")

    confidence, confidence_reason = activity_confidence(page, metadata["activity_type"], tags)
    if confidence == "low":
        reasons.append(f"activity_type confidence low: {confidence_reason}")

    if not metadata["topics"]:
        reasons.append("topics are empty")

    year_match = re.search(r"content/(\d{4})/", page.rel_path)
    if year_match and int(year_match.group(1)) < 2015:
        reasons.append("old pre-2015 content")

    title = str(page.params.get("title", ""))
    if len(title) > 180 or title.count("-") > 8:
        reasons.append("unusual title shape")

    return reasons


def metadata_lines(metadata: dict[str, Any]) -> list[str]:
    lines = []
    for field in METADATA_FIELDS:
        value = metadata[field]
        if isinstance(value, list):
            inner = ", ".join(f'"{item}"' for item in value)
            lines.append(f"{field}: [{inner}]")
        elif isinstance(value, bool):
            lines.append(f"{field}: {'true' if value else 'false'}")
        elif value == "":
            lines.append(f'{field}: ""')
        else:
            lines.append(f"{field}: {value}")
    return lines


def insert_metadata(page: Page, metadata: dict[str, Any]) -> str:
    text = page.path.read_text(encoding="utf-8")
    fm_type, fm_body, rest = split_frontmatter(text)
    if fm_type != "yaml":
        raise ValueError(f"Cannot apply to non-YAML file: {page.rel_path}")
    return f"---\n{fm_body.rstrip()}\n" + "\n".join(metadata_lines(metadata)) + f"\n---\n{rest}"


def md_escape(value: Any) -> str:
    if isinstance(value, list):
        value = ", ".join(value)
    text = str(value).replace("\n", " ").replace("\r", " ")
    return text.replace("|", "\\|")


def example_diff(page: Page, metadata: dict[str, Any]) -> str:
    title = str(page.params.get("title", ""))
    lines = ["```diff", f"--- {page.rel_path}", f"+++ {page.rel_path}", "@@ front matter @@"]
    if title:
        lines.append(f" title: {title}")
    for line in metadata_lines(metadata):
        lines.append(f"+{line}")
    lines.append("```")
    return "\n".join(lines)


def write_dry_run_report(
    pages: list[Page],
    skipped: list[tuple[Page, str]],
    existing: list[tuple[Page, str]],
    proposed: list[Proposal],
    manual_review: list[tuple[Page, str]],
    report_path: Path,
    apply: bool,
    only_activity_type: str | None,
) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    activity_counts = Counter(p.metadata["activity_type"] for p in proposed)
    language_counts = Counter(p.metadata["language"] for p in proposed)
    topic_counts: Counter[str] = Counter()
    for proposal in proposed:
        topic_counts.update(proposal.metadata["topics"])

    changed_to_ja = [
        proposal
        for proposal in proposed
        if proposal.metadata["language"] == "ja"
        and "Japanese body text" in " ".join(proposal.warnings + [proposal.reason])
    ][:10]
    mixed_examples = [proposal for proposal in proposed if proposal.metadata["language"] == "mixed"][:5]

    action_label = "updated" if apply else "proposed for automatic update"
    mode_text = "--apply" if apply else "--dry-run"
    filter_text = f" --only-activity-type {only_activity_type}" if only_activity_type else ""
    title = "Activity Metadata Monthly Apply" if apply and only_activity_type == "monthly_report" else "Activity Metadata Bulk Dry Run"
    no_content_text = (
        "Monthly report metadata was applied only to filtered files."
        if apply
        else "No content files were modified. This report proposes metadata only."
    )

    lines = [
        f"# {title}",
        "",
        f"Generated by `tools/apply_activity_metadata.py {mode_text}{filter_text}`.",
        "",
        no_content_text,
        "",
        "## Rule Changes In This Run",
        "",
        "- Language detection now uses cleaned main body text only.",
        "- Front matter, title-only signals, tags, URLs, Markdown links/images, code spans/blocks, HTML snippets, and Markdown syntax are ignored for language counts.",
        "- Japanese characters count Hiragana, Katakana, and Kanji.",
        "- English counts Latin alphabet words after body cleanup.",
        "- `mixed` requires at least 300 Japanese characters and at least 150 English words.",
        "- Low-confidence language, weak activity type confidence, empty topics, strong title/body language disagreement, old pre-2015 content, and unusual title shapes are sent to manual review.",
        "",
        "## Summary",
        "",
        f"- total files considered: {len(pages)}",
        f"- files skipped: {len(skipped)}",
        f"- files that already have metadata: {len(existing)}",
        f"- files {action_label}: {len(proposed)}",
        f"- files requiring manual review: {len(manual_review)}",
        f"- activity filter: {only_activity_type or 'none'}",
        "",
        "## Metadata Added Summary",
        "",
        "- Added fields: `activity_type`, `source_platform`, `source_url`, `language`, `topics`, `featured`",
        "- Existing title/date/slug/aliases/cover/tags/body were preserved.",
        "- Existing complete metadata records were skipped.",
        "",
        "## Candidate Counts By Activity Type",
        "",
    ]
    for key, value in sorted(activity_counts.items()):
        lines.append(f"- {key}: {value}")

    lines.extend(["", "## Candidate Counts By Language", ""])
    for key, value in sorted(language_counts.items()):
        lines.append(f"- {key}: {value}")

    lines.extend(["", "## Candidate Counts By Topic", ""])
    for key, value in sorted(topic_counts.items()):
        lines.append(f"- {key}: {value}")

    lines.extend(["", "## Files Skipped", "", "| file | reason |", "| --- | --- |"])
    for page, reason in skipped:
        lines.append(f"| `{md_escape(page.rel_path)}` | {md_escape(reason)} |")

    lines.extend(["", "## Files Already With Metadata", "", "| file | status |", "| --- | --- |"])
    for page, status in existing:
        lines.append(f"| `{md_escape(page.rel_path)}` | {md_escape(status)} |")

    lines.extend(
        [
            "",
            "## Updated Files" if apply else "## Proposed Automatic Updates",
            "",
            "| file | title | activity_type | source_platform | language | topics | reason |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for proposal in proposed:
        page = proposal.page
        metadata = proposal.metadata
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{md_escape(page.rel_path)}`",
                    md_escape(page.params.get("title", "")),
                    md_escape(metadata["activity_type"]),
                    md_escape(metadata["source_platform"]),
                    md_escape(metadata["language"]),
                    md_escape(metadata["topics"]),
                    md_escape(proposal.reason),
                ]
            )
            + " |"
        )

    lines.extend(["", "## Files Requiring Manual Review", "", "| file | reason |", "| --- | --- |"])
    for page, reason in manual_review:
        lines.append(f"| `{md_escape(page.rel_path)}` | {md_escape(reason)} |")

    lines.extend(
        [
            "",
            "## 10 Examples Changed From Mixed To Ja",
            "",
            "| file | title | reason |",
            "| --- | --- | --- |",
        ]
    )
    for proposal in changed_to_ja:
        lines.append(
            f"| `{md_escape(proposal.page.rel_path)}` | {md_escape(proposal.page.params.get('title', ''))} | {md_escape('; '.join(proposal.warnings))} |"
        )

    lines.extend(
        [
            "",
            "## 5 Examples Remaining Mixed",
            "",
            "| file | title | reason |",
            "| --- | --- | --- |",
        ]
    )
    for proposal in mixed_examples:
        lines.append(
            f"| `{md_escape(proposal.page.rel_path)}` | {md_escape(proposal.page.params.get('title', ''))} | {md_escape('; '.join(proposal.warnings))} |"
        )

    lines.extend(["", "## 20 Example Proposed Diffs", ""])
    for proposal in proposed[:20]:
        lines.append(example_diff(proposal.page, proposal.metadata))
        lines.append("")

    report_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def run(apply: bool, report_path: Path, only_activity_type: str | None) -> int:
    manual_reasons = audit_manual_reasons(AUDIT_REPORT)
    pages = [load_page(path) for path in sorted(CONTENT_ROOT.rglob("*.md"))]
    skipped: list[tuple[Page, str]] = []
    existing: list[tuple[Page, str]] = []
    proposed: list[Proposal] = []
    manual_review: list[tuple[Page, str]] = []

    for page in pages:
        reason = skip_reason(page, manual_reasons)
        if reason:
            skipped.append((page, reason))
            continue

        if has_existing_metadata(page):
            valid, status = existing_metadata_valid(page)
            existing_activity_type = str(page.params.get("activity_type", ""))
            if only_activity_type and existing_activity_type != only_activity_type:
                skipped.append((page, f"outside activity filter: {existing_activity_type or 'unknown'}"))
                continue
            existing.append((page, status))
            if not valid:
                manual_review.append((page, f"existing metadata needs review: {status}"))
            continue

        metadata, language_signal = proposed_metadata(page)
        if only_activity_type and metadata["activity_type"] != only_activity_type:
            skipped.append((page, f"outside activity filter: {metadata['activity_type']}"))
            continue
        if metadata["activity_type"] == "book":
            manual_review.append((page, "possible dedicated book page; do not auto-classify book objects yet"))
            continue
        reasons = review_reasons(page, metadata, language_signal)
        language_reason = (
            f"{language_signal.reason} ({language_signal.japanese_chars} Japanese chars, "
            f"{language_signal.english_words} English words)"
        )
        if reasons:
            manual_review.append((page, "; ".join(reasons)))
            continue
        proposed.append(
            Proposal(
                page,
                metadata,
                "safe regular dated Markdown content with missing activity metadata",
                [language_reason],
            )
        )

    write_dry_run_report(pages, skipped, existing, proposed, manual_review, report_path, apply, only_activity_type)

    if apply:
        for proposal in proposed:
            proposal.page.path.write_text(insert_metadata(proposal.page, proposal.metadata), encoding="utf-8")

    print(f"Total files considered: {len(pages)}")
    print(f"Skipped: {len(skipped)}")
    print(f"Already with metadata: {len(existing)}")
    print(f"{'Applied updates' if apply else 'Proposed automatic updates'}: {len(proposed)}")
    print(f"Manual review: {len(manual_review)}")
    print(f"Report: {report_path}")
    if apply:
        print("Applied proposed metadata updates.")
    else:
        print("Dry-run only. No content files were modified.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare/apply activity metadata to Hugo Markdown content.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="Report proposed changes only.")
    mode.add_argument("--apply", action="store_true", help="Write proposed metadata to content files.")
    parser.add_argument("--report", type=Path, default=DRY_RUN_REPORT)
    parser.add_argument("--only-activity-type", choices=sorted(VALID_ACTIVITY_TYPES), default=None)
    args = parser.parse_args()
    return run(apply=args.apply, report_path=args.report.resolve(), only_activity_type=args.only_activity_type)


if __name__ == "__main__":
    raise SystemExit(main())
