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
DEFAULT_REPORT = ROOT / "reports" / "activity-metadata-audit.md"

KNOWN_SECTIONS = {
    "archive",
    "fabcross",
    "posts",
    "shenzhen",
    "teardown",
}

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
    ("community", ("community", "コミュニティ", "nt", "nico-tech", "ニコ技")),
    ("education", ("education", "stem", "steam", "university", "大学", "講義")),
    ("event", ("event", "meetup", "conference", "tour", "イベント", "ミートアップ", "観察会")),
    ("podcast", ("podcast", "ポッドキャスト")),
    ("book", ("book", "書籍", "出版")),
]


@dataclass
class AuditRow:
    path: str
    section: str
    title: str
    date: str
    draft: str
    activity_type: str
    activity_type_status: str
    source_platform: str
    source_platform_status: str
    language_candidate: str
    content_type_candidate: str
    topics_candidate: list[str]
    tags: list[str]
    safe_for_auto_update: bool
    manual_review_reason: str


def split_frontmatter(text: str) -> tuple[str | None, str, str]:
    if text.startswith("---\n") or text.startswith("---\r\n"):
        match = re.match(r"^---\s*\r?\n(.*?)\r?\n---\s*\r?\n(.*)$", text, re.S)
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
        item = double or single or bare
        item = strip_quotes(item.strip())
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

        if fm_type == "yaml":
            match = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", line)
            separator = ":"
        else:
            match = re.match(r"^([A-Za-z0-9_-]+)\s*=\s*(.*)$", line)
            separator = "="

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
            if separator == "=":
                raw_value = re.split(r"\s+#", raw_value, maxsplit=1)[0].strip()
            params[key] = strip_quotes(raw_value)
        i += 1
    return params


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def detect_section(path: Path) -> str:
    rel_parts = path.relative_to(CONTENT_ROOT).parts
    if not rel_parts:
        return ""
    if len(rel_parts) == 1:
        return "root"
    first = rel_parts[0]
    if first in KNOWN_SECTIONS:
        return first
    if re.fullmatch(r"\d{4}", first):
        return "year-bundle"
    return first


def detect_language(title: str, body: str) -> str:
    sample = f"{title}\n{body[:4000]}"
    kana = len(re.findall(r"[\u3040-\u30ff]", sample))
    cjk = len(re.findall(r"[\u4e00-\u9fff]", sample))
    latin_words = len(re.findall(r"[A-Za-z]{3,}", sample))
    if kana >= 10 and latin_words >= 50:
        return "ja-en"
    if kana >= 10:
        return "ja"
    if cjk >= 20 and latin_words < 50:
        return "zh"
    if latin_words >= 20:
        return "en"
    if cjk > 0:
        return "cjk"
    return "unknown"


def has_any(text: str, needles: tuple[str, ...]) -> bool:
    return any(needle in text for needle in needles)


def has_word(text: str, word: str) -> bool:
    return re.search(rf"(?<![a-z0-9]){re.escape(word)}(?![a-z0-9])", text) is not None


def detect_content_type(path: Path, title: str, tags: list[str]) -> str:
    strong_text = f" {title} {' '.join(tags)} {rel(path)} ".lower()
    if "monthly-report" in {tag.lower() for tag in tags} or has_any(
        strong_text,
        ("月次報告", "monthly report", "monthly news", "monthly-report"),
    ):
        return "monthly_report"
    if has_any(strong_text, ("podcast", "ポッドキャスト")):
        return "podcast"
    if has_any(strong_text, ("youtube", "youtu.be", " video", " videos", "動画", "映像")):
        return "video"
    if has_word(strong_text, "paper") or has_any(strong_text, ("論文", "research-at-scale", "research at scale")):
        return "paper"
    if has_word(strong_text, "book") or has_any(
        strong_text,
        ("書籍", "出版", "prototype city", "hardware hacker", "makers ecosystem", "メイカーズのエコシステム"),
    ):
        return "book"
    if has_any(strong_text, ("talk", "presentation", "講演", "登壇", "lecture", "講義")):
        return "talk"
    if has_any(strong_text, ("event", "meetup", "conference", "tour", "イベント", "ミートアップ", "観察会")):
        return "event"
    return "post"


def detect_topics(title: str, tags: list[str], section: str, body: str) -> list[str]:
    haystack = f" {title} {' '.join(tags)} {section} {body[:2000]} ".lower()
    topics = {section} if section in {"archive", "fabcross", "shenzhen", "teardown"} else set()
    for topic, needles in TOPIC_RULES:
        if has_any(haystack, tuple(needle.lower() for needle in needles)):
            topics.add(topic)
    return sorted(topics)


def bool_param(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() == "true"


def classify_file(path: Path, params: dict[str, Any], fm_type: str | None) -> tuple[bool, str]:
    rel_path = rel(path)
    name = path.name
    section = detect_section(path)
    reasons: list[str] = []

    if fm_type is None:
        reasons.append("missing frontmatter")
    if name == "_index.md":
        reasons.append("section/list page")
    if rel_path in {"content/about.md", "content/search.md", "content/_index.md"}:
        reasons.append("site page")
    if bool_param(params.get("draft", False)):
        reasons.append("draft")
    if not params.get("title"):
        reasons.append("missing title")
    if not params.get("date") and name != "_index.md":
        reasons.append("missing date")
    if section not in KNOWN_SECTIONS and section != "year-bundle":
        reasons.append(f"non-post section: {section or 'root'}")

    safe = not reasons
    return safe, "; ".join(reasons) if reasons else "safe regular dated content"


def audit_file(path: Path) -> AuditRow:
    text = path.read_text(encoding="utf-8")
    fm_type, fm_body, body = split_frontmatter(text)
    params = parse_frontmatter(fm_type, fm_body)
    tags = params.get("tags", [])
    if isinstance(tags, str):
        tags = [tags] if tags else []
    elif not isinstance(tags, list):
        tags = []

    title = str(params.get("title", ""))
    section = detect_section(path)
    activity_type = str(params.get("activity_type", ""))
    source_platform = str(params.get("source_platform", ""))
    safe, reason = classify_file(path, params, fm_type)

    return AuditRow(
        path=rel(path),
        section=section,
        title=title,
        date=str(params.get("date", "")),
        draft=str(bool_param(params.get("draft", False))).lower(),
        activity_type=activity_type or "(missing)",
        activity_type_status="existing" if activity_type else "missing",
        source_platform=source_platform or "(missing)",
        source_platform_status="existing" if source_platform else "missing",
        language_candidate=detect_language(title, body),
        content_type_candidate=detect_content_type(path, title, tags),
        topics_candidate=detect_topics(title, tags, section, body),
        tags=tags,
        safe_for_auto_update=safe,
        manual_review_reason="" if safe else reason,
    )


def md_escape(value: Any) -> str:
    if isinstance(value, list):
        value = ", ".join(value)
    text = str(value)
    text = text.replace("\n", " ").replace("\r", " ")
    text = text.replace("|", "\\|")
    return text


def write_report(rows: list[AuditRow], report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)

    counters = {
        "total_markdown_files": len(rows),
        "activity_type_existing": sum(row.activity_type_status == "existing" for row in rows),
        "activity_type_missing": sum(row.activity_type_status == "missing" for row in rows),
        "source_platform_existing": sum(row.source_platform_status == "existing" for row in rows),
        "source_platform_missing": sum(row.source_platform_status == "missing" for row in rows),
        "safe_for_auto_update": sum(row.safe_for_auto_update for row in rows),
        "manual_review": sum(not row.safe_for_auto_update for row in rows),
    }
    section_counts = Counter(row.section for row in rows)
    language_counts = Counter(row.language_candidate for row in rows)
    content_type_counts = Counter(row.content_type_candidate for row in rows)

    lines = [
        "# Activity Metadata Audit",
        "",
        "Generated by `tools/audit_activity_metadata.py`.",
        "",
        "This is a read-only audit of Markdown files under `content/`. Generated redirect HTML stubs are excluded because the audit only scans `*.md` source files.",
        "",
        "## Summary",
        "",
    ]
    for key, value in counters.items():
        lines.append(f"- {key}: {value}")

    lines.extend(["", "## Sections", ""])
    for key, value in sorted(section_counts.items()):
        lines.append(f"- {key}: {value}")

    lines.extend(["", "## Language Candidates", ""])
    for key, value in sorted(language_counts.items()):
        lines.append(f"- {key}: {value}")

    lines.extend(["", "## Content Type Candidates", ""])
    for key, value in sorted(content_type_counts.items()):
        lines.append(f"- {key}: {value}")

    lines.extend(
        [
            "",
            "## Files Requiring Manual Review",
            "",
            "| path | reason |",
            "| --- | --- |",
        ]
    )
    for row in rows:
        if not row.safe_for_auto_update:
            lines.append(f"| `{md_escape(row.path)}` | {md_escape(row.manual_review_reason)} |")

    lines.extend(
        [
            "",
            "## Detailed Audit",
            "",
            "| path | title | section | draft | activity_type | activity_type_status | source_platform | source_platform_status | language_candidate | content_type_candidate | topics_candidate | tags | safe_for_auto_update | manual_review_reason |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{md_escape(row.path)}`",
                    md_escape(row.title),
                    md_escape(row.section),
                    md_escape(row.draft),
                    md_escape(row.activity_type),
                    md_escape(row.activity_type_status),
                    md_escape(row.source_platform),
                    md_escape(row.source_platform_status),
                    md_escape(row.language_candidate),
                    md_escape(row.content_type_candidate),
                    md_escape(row.topics_candidate),
                    md_escape(row.tags),
                    "yes" if row.safe_for_auto_update else "no",
                    md_escape(row.manual_review_reason),
                ]
            )
            + " |"
        )

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit activity metadata candidates for Hugo content.")
    parser.add_argument("--content-root", type=Path, default=CONTENT_ROOT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    content_root = args.content_root.resolve()
    rows = [audit_file(path) for path in sorted(content_root.rglob("*.md"))]
    write_report(rows, args.report.resolve())

    print(f"Audited Markdown files: {len(rows)}")
    print(f"Report: {args.report}")
    print(f"activity_type existing: {sum(row.activity_type_status == 'existing' for row in rows)}")
    print(f"activity_type missing: {sum(row.activity_type_status == 'missing' for row in rows)}")
    print(f"source_platform existing: {sum(row.source_platform_status == 'existing' for row in rows)}")
    print(f"source_platform missing: {sum(row.source_platform_status == 'missing' for row in rows)}")
    print(f"safe for automatic metadata update: {sum(row.safe_for_auto_update for row in rows)}")
    print(f"manual review required: {sum(not row.safe_for_auto_update for row in rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
