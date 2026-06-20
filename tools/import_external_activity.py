#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from audit_external_activity_sources import (
    ROOT,
    SourceResult,
    audit_source,
    find_duplicates,
    load_config,
    md_escape,
)

DEFAULT_CONFIG = ROOT / "tools" / "activity_sources.json"
FALLBACK_CONFIG = ROOT / "tools" / "activity_sources.example.json"
DEFAULT_OUTPUT = ROOT / "data" / "activity" / "external_updates.json"
DEFAULT_DRY_RUN_REPORT = ROOT / "reports" / "external-activity-import-dry-run.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import external activity feed items.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true", help="Fetch and report proposed records without writing JSON.")
    mode.add_argument("--write", action="store_true", help="Write normalized records to data/activity/external_updates.json.")
    parser.add_argument("--config", type=Path, default=None)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--report", type=Path, default=DEFAULT_DRY_RUN_REPORT)
    return parser.parse_args()


def resolve_config(config: Path | None) -> Path:
    if config:
        return config if config.is_absolute() else ROOT / config
    if DEFAULT_CONFIG.exists():
        return DEFAULT_CONFIG
    return FALLBACK_CONFIG


def sort_key(item: dict[str, Any]) -> str:
    return str(item.get("date", ""))


def collect_items(results: list[SourceResult]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for result in results:
        items.extend(result.items)
    return sorted(items, key=sort_key, reverse=True)


def duplicate_url_groups(items: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in items:
        url = str(item.get("source_url", "")).strip()
        if url:
            grouped[url].append(item)
    return {url: group for url, group in grouped.items() if len(group) > 1}


def is_safe_to_write(results: list[SourceResult]) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    failed = [result.source.get("id", "") for result in results if result.status == "failed"]
    skipped = [result.source.get("id", "") for result in results if result.status == "skipped"]
    if failed:
        reasons.append("Some sources failed: " + ", ".join(failed))
    if skipped:
        reasons.append("Some sources were skipped: " + ", ".join(skipped))
    return not reasons, reasons


def write_json_output(path: Path, items: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "items": items,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_report(
    path: Path,
    config_path: Path,
    output_path: Path,
    results: list[SourceResult],
    items: list[dict[str, Any]],
    duplicate_warnings: list[str],
    duplicate_groups: dict[str, list[dict[str, Any]]],
    dry_run: bool,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    by_source = Counter(str(item.get("source_id", "")) for item in items)
    by_activity = Counter(str(item.get("activity_type", "")) for item in items)
    by_language = Counter(str(item.get("language", "")) for item in items)
    safe, unsafe_reasons = is_safe_to_write(results)

    lines: list[str] = []
    lines.append("# External Activity Import Dry Run")
    lines.append("")
    lines.append(f"Generated: `{datetime.now(timezone.utc).isoformat()}`")
    lines.append("")
    lines.append(f"- mode: `{'dry-run' if dry_run else 'write'}`")
    lines.append(f"- config used: `{config_path.relative_to(ROOT)}`")
    lines.append(f"- proposed output path: `{output_path.relative_to(ROOT)}`")
    lines.append(f"- JSON written: `{'no' if dry_run else 'yes'}`")
    lines.append("")
    lines.append("This run does not modify existing content posts, metadata, `public/`, homepage, navigation, config, templates, or GitHub Actions.")
    lines.append("")

    lines.append("## Source Results")
    lines.append("")
    lines.append("| source_id | feed_url | platform | activity_type | language | status | items | issues |")
    lines.append("| --- | --- | --- | --- | --- | --- | ---: | --- |")
    for result in results:
        source = result.source
        lines.append(
            "| "
            + " | ".join(
                [
                    md_escape(source.get("id", "")),
                    md_escape(source.get("feed_url", "")),
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

    lines.append("## Counts By Source")
    lines.append("")
    for key, count in sorted(by_source.items()):
        lines.append(f"- `{key}`: {count}")
    if not by_source:
        lines.append("- No items normalized.")
    lines.append("")

    lines.append("## Counts By Activity Type")
    lines.append("")
    for key, count in sorted(by_activity.items()):
        lines.append(f"- `{key}`: {count}")
    if not by_activity:
        lines.append("- No items normalized.")
    lines.append("")

    lines.append("## Counts By Language")
    lines.append("")
    for key, count in sorted(by_language.items()):
        lines.append(f"- `{key}`: {count}")
    if not by_language:
        lines.append("- No items normalized.")
    lines.append("")

    lines.append("## Duplicate URL Warnings")
    lines.append("")
    if duplicate_warnings:
        for warning in duplicate_warnings:
            lines.append(f"- {warning}")
    else:
        lines.append("- No duplicate normalized IDs or source URLs found.")
    lines.append("")
    if duplicate_groups:
        lines.append("Recommendation for future `/updates/` display: hide duplicate source URLs by default and show the newest or preferred-language variant, while retaining both records in data for language/source-specific views.")
    else:
        lines.append("Recommendation for future `/updates/` display: no duplicate URL handling is needed for this run.")
    lines.append("")

    lines.append("## Sample Normalized Records")
    lines.append("")
    if items:
        lines.append("```json")
        lines.append(json.dumps(items[:10], ensure_ascii=False, indent=2))
        lines.append("```")
    else:
        lines.append("_No records normalized._")
    lines.append("")

    lines.append("## Safe To Run `--write` Next?")
    lines.append("")
    if safe:
        lines.append("Yes, with one caveat: duplicate source URLs should be accepted as known warnings or handled by display logic later. This importer will not remove duplicates yet.")
    else:
        lines.append("No.")
        for reason in unsafe_reasons:
            lines.append(f"- {reason}")
    lines.append("")

    lines.append("## Recommended Next Step")
    lines.append("")
    lines.append("Review this dry-run report. If the counts, sample records, and duplicate URL warnings are acceptable, run `tools/import_external_activity.py --write` in a later step to create `data/activity/external_updates.json`.")
    lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    args = parse_args()
    config_path = resolve_config(args.config)
    output_path = args.output if args.output.is_absolute() else ROOT / args.output
    report_path = args.report if args.report.is_absolute() else ROOT / args.report

    sources = load_config(config_path)
    imported_at = datetime.now(timezone.utc).isoformat()
    results = [audit_source(source, imported_at) for source in sources]
    items = collect_items(results)
    duplicate_warnings = find_duplicates(results)
    duplicate_groups = duplicate_url_groups(items)

    if args.write:
        write_json_output(output_path, items)

    write_report(
        report_path,
        config_path,
        output_path,
        results,
        items,
        duplicate_warnings,
        duplicate_groups,
        dry_run=args.dry_run,
    )

    tested = sum(1 for result in results if result.status == "tested")
    skipped = sum(1 for result in results if result.status == "skipped")
    failed = sum(1 for result in results if result.status == "failed")
    print("External activity import dry run complete." if args.dry_run else "External activity import write complete.")
    print(f"Sources: {len(results)} total, {tested} tested, {skipped} skipped, {failed} failed.")
    print(f"Normalized items: {len(items)}")
    print(f"Duplicate warnings: {len(duplicate_warnings)}")
    print(f"Report: {report_path.relative_to(ROOT)}")
    if args.write:
        print(f"Wrote: {output_path.relative_to(ROOT)}")
    else:
        print(f"Proposed output: {output_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
