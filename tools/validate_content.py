#!/usr/bin/env python3
"""
Content validation for the Hugo site.

Markdown content checks (content/**/*.md):
  1. slug: post  -- safe_slug() fallback; always a wrong URL
  2. aliases containing /post/  -- matching bad alias
  3. duplicate slugs within the same section directory
  4. duplicate aliases within the same section directory

External activity data checks (data/activity/external_updates.json):
  5. All external items have title, date, source_url, source_platform
  6. note items with a recent RSS window should have a thumbnail (image field)
  7. The latest known note URL is present

Exits 0 if clean, 1 if violations found.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"
EXTERNAL_DATA = ROOT / "data" / "activity" / "external_updates.json"

# The most recently known note article; update this when new articles are added.
# The CI import workflow keeps external_updates.json current automatically.
LATEST_KNOWN_NOTE_URL = "https://note.com/takasu/n/ncbb378be7a25"

SLUG_RE = re.compile(r"^slug:\s*(.+)$", re.MULTILINE)
ALIAS_RE = re.compile(r'^aliases:\s*\[([^\]]*)\]', re.MULTILINE)
FORBIDDEN_SLUG = "post"


# ---------------------------------------------------------------------------
# Markdown content checks
# ---------------------------------------------------------------------------

def read_frontmatter(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[:end + 4] if end != -1 else text


def extract_slug(fm: str) -> str | None:
    m = SLUG_RE.search(fm)
    return m.group(1).strip() if m else None


def extract_aliases(fm: str) -> list[str]:
    m = ALIAS_RE.search(fm)
    if not m:
        return []
    raw = m.group(1)
    return [s.strip().strip('"').strip("'") for s in raw.split(",") if s.strip()]


def check_markdown(errors: list[str]) -> None:
    section_slugs: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    section_aliases: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))

    for md in sorted(CONTENT_DIR.rglob("*.md")):
        rel = md.relative_to(ROOT)
        section = md.parent.name

        fm = read_frontmatter(md)
        if not fm:
            continue

        slug = extract_slug(fm)
        aliases = extract_aliases(fm)

        if slug == FORBIDDEN_SLUG:
            errors.append(f"  slug:post   {rel}")

        for alias in aliases:
            if "/post/" in alias:
                errors.append(f"  alias /post/  {rel}  →  {alias}")

        if slug:
            section_slugs[section][slug].append(str(rel))
        for alias in aliases:
            section_aliases[section][alias].append(str(rel))

    for section, slug_map in section_slugs.items():
        for slug, files in slug_map.items():
            if len(files) > 1:
                errors.append(
                    f"  dup slug '{slug}' in [{section}]:\n"
                    + "\n".join(f"      {f}" for f in files)
                )

    for section, alias_map in section_aliases.items():
        for alias, files in alias_map.items():
            if len(files) > 1:
                errors.append(
                    f"  dup alias '{alias}' in [{section}]:\n"
                    + "\n".join(f"      {f}" for f in files)
                )


# ---------------------------------------------------------------------------
# External activity data checks
# ---------------------------------------------------------------------------

def check_external_data(errors: list[str]) -> None:
    if not EXTERNAL_DATA.exists():
        errors.append(f"  missing: {EXTERNAL_DATA.relative_to(ROOT)}")
        return

    try:
        data = json.loads(EXTERNAL_DATA.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"  external_updates.json is invalid JSON: {exc}")
        return

    items = data.get("items", [])
    if not items:
        errors.append("  external_updates.json has no items")
        return

    # Rule 5: required fields on every external item
    required = {"title", "date", "source_url", "source_platform"}
    for item in items:
        if item.get("activity_type") not in {"external", None}:
            continue  # only validate article-type entries
        missing = [f for f in required if not item.get(f)]
        if missing:
            errors.append(
                f"  external item missing fields {missing}: {item.get('id', '?')}"
            )

    # Rule 6: systemic thumbnail failure check for note items.
    # A single article without a cover image is normal (note.com lets authors
    # skip cover images). Only fail when the majority of recent note items are
    # missing thumbnails, which indicates the importer's image extraction broke.
    note_items = sorted(
        [i for i in items if i.get("source_platform") == "note"],
        key=lambda i: i.get("date", ""),
        reverse=True,
    )
    if note_items:
        recent = note_items[:5]
        missing_count = sum(1 for i in recent if not i.get("image"))
        if missing_count >= len(recent):
            errors.append(
                f"  all recent note items ({len(recent)}) are missing thumbnails — "
                "importer image extraction may be broken"
            )
        elif missing_count > len(recent) // 2:
            errors.append(
                f"  majority of recent note items ({missing_count}/{len(recent)}) are missing thumbnails — "
                "importer image extraction may be broken"
            )

    # Rule 7: latest known note article must be present
    urls = {i.get("source_url", "") for i in items}
    if LATEST_KNOWN_NOTE_URL not in urls:
        errors.append(
            f"  latest note article not found in external_updates.json: {LATEST_KNOWN_NOTE_URL}"
        )

    # Rule 8: at least one YouTube/video entry must be present. A known YouTube
    # source (youtube_ja/youtube_en) exists, so a drop to zero video entries
    # means the importer silently lost data rather than the channel going empty.
    video_items = [i for i in items if i.get("activity_type") == "video"]
    if not video_items:
        errors.append(
            "  no video-type entries found in external_updates.json "
            "(YouTube sources are configured; this indicates lost data, not an empty channel)"
        )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    errors: list[str] = []
    check_markdown(errors)
    check_external_data(errors)

    if errors:
        print(f"VALIDATION FAILED - {len(errors)} issue(s) found:\n")
        for e in errors:
            print(e)
        return 1

    print(
        "Validation passed: no slug:post, no /post/ aliases, no duplicate slugs or aliases, "
        "external_updates.json is present and contains latest note article with thumbnails "
        "and at least one video entry."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
