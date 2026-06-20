# External Activity Image Audit

Generated: `2026-06-20`

Scope: YouTube RSS thumbnails only for `youtube_ja`, `youtube_en`, and `youtube_talks`.

## RSS Thumbnail Fields

The configured YouTube feeds expose thumbnail URLs in `media:group` / `media:thumbnail`.

| source_id | entries checked | direct media:thumbnail | media:group/media:thumbnail | sample |
| --- | ---: | ---: | ---: | --- |
| `youtube_ja` | 12 | 0 | 12 | `https://i2.ytimg.com/vi/UVJQNMm7wJk/hqdefault.jpg` |
| `youtube_en` | 4 | 0 | 4 | `https://i1.ytimg.com/vi/xAotcCqOcug/hqdefault.jpg` |
| `youtube_talks` | 13 | 0 | 13 | `https://i4.ytimg.com/vi/WArYVtr-pzM/hqdefault.jpg` |

No YouTube watch pages were fetched, and the YouTube API was not used.

## Import Result

| source_id | YouTube items | items with image |
| --- | ---: | ---: |
| `youtube_ja` | 12 | 12 |
| `youtube_en` | 4 | 4 |
| `youtube_talks` | 13 | 13 |
| **Total** | **29** | **29** |

Sample imported image URL: `https://i1.ytimg.com/vi/xAotcCqOcug/hqdefault.jpg`

Non-YouTube items with image after this run: `0`.

## Importer Change

The importer now uses YouTube RSS-provided `media:thumbnail` elements under `media:group` for YouTube Atom entries. It does not synthesize thumbnail URLs from video IDs.

Existing non-YouTube image extraction behavior is unchanged.

## Homepage Display

`layouts/partials/home_activity_card.html` already renders the `image` field when present, so homepage cards can display these YouTube thumbnails without a layout change.
