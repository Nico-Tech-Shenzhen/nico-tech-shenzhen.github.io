# Posfie Event Report Source Audit

Generated: `2026-06-20`

Source checked: `https://posfie.com/@tks`

## Findings

- The profile page is fetchable and returns HTML.
- The page advertises an RSS feed: `https://posfie.com/@tks/rss`.
- The profile page includes a stable favicon URL: `https://s.tgstc.com/static/web/img/posfie/icon/favicon.ico`.
- The RSS feed is fetchable and returns RSS 2.0 XML.
- RSS items include stable metadata useful for import: `guid`, `title`, `link`, `description`, and `pubDate`.
- The feed description says the profile has 321 summaries; the fetched feed exposes recent items.

## Decision

Automatic extraction appears feasible from the RSS feed, but this task did not implement importer/config changes because the active source configuration file is outside the allowed file list for this task.

Static link fallback was used:

- Label: `参加イベントレポート / Event Reports`
- URL: `https://posfie.com/@tks`
- Favicon: `https://s.tgstc.com/static/web/img/posfie/icon/favicon.ico`

## Later Importer Notes

If Posfie is imported later, use only the RSS feed advertised by the profile page.

Suggested normalized fields:

- `source_platform`: `posfie`
- `source_label`: `Posfie`
- `activity_type`: `event_report`
- `language`: `ja`
- `source_icon`: `https://s.tgstc.com/static/web/img/posfie/icon/favicon.ico`
