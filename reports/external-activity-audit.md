# External Activity Feed Audit

Generated: `2026-06-19T23:44:34.697598+00:00`

This is a read-only prototype audit. It normalizes feed entries in memory and does not write `data/activity/*.json`, Markdown posts, `public/`, templates, config, navigation, or homepage files.

## Source Config Format

Config file: `tools\activity_sources.example.json`

Each source has:

- `id`: stable source ID, for example `youtube_ja` or `youtube_en`
- `label`: human-readable source name
- `source_platform`: `youtube`, `podcast`, `medium`, or `note`
- `activity_type`: `video`, `podcast`, or `external`
- `language`: default language for items from this source
- `feed_url`: RSS/Atom feed URL
- `site_url`: public profile/channel URL
- `enabled`: whether the source should be tested

YouTube sources are intentionally separate: `youtube_ja` uses IDs like `youtube:ja:VIDEO_ID`; `youtube_en` uses IDs like `youtube:en:VIDEO_ID`.

## Sources Tested

| source_id | platform | activity_type | language | status | items | issues |
| --- | --- | --- | --- | --- | ---: | --- |
| youtube_ja | youtube | video | ja | skipped | 0 | No real feed_url configured yet. |
| youtube_en | youtube | video | en | skipped | 0 | No real feed_url configured yet. |
| podcast_main | podcast | podcast | ja | skipped | 0 | No real feed_url configured yet. |
| medium_main | medium | external | ja | skipped | 0 | No real feed_url configured yet. |
| note_main | note | external | ja | skipped | 0 | No real feed_url configured yet. |

## Sample Normalized Items

### youtube_ja

_No items normalized._

### youtube_en

_No items normalized._

### podcast_main

_No items normalized._

### medium_main

_No items normalized._

### note_main

_No items normalized._

## Duplicate Warnings

- No duplicate normalized IDs or source URLs found among normalized items.

## Parsing Issues

- `youtube_ja`: No real feed_url configured yet.
- `youtube_en`: No real feed_url configured yet.
- `podcast_main`: No real feed_url configured yet.
- `medium_main`: No real feed_url configured yet.
- `note_main`: No real feed_url configured yet.

## Recommended Next Step

Replace placeholder `feed_url` values with real source feeds, then re-run this audit. After the normalized samples look correct, add a dry-run importer that writes proposed `data/activity/*.json` changes to a report before enabling persistent data output.
