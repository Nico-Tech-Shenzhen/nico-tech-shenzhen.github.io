# Search Index Debug

Date: 2026-06-20

## Deployed Index Check

Fetched `https://takasumasakazu.net/index.json` successfully.

- HTTP status: 200
- Content-Type: `application/json; charset=utf-8`
- JSON parse: valid
- Record count: 739
- Records with `external: true`: 0

String checks against the deployed JSON:

- `10ドルの偽AirPods`: not found
- `What $10 Fake AirPods`: found
- `Nico-Tech Shenzhen Field Notes`: found
- `researchmap`: found
- `note`: found
- `youtube`: found

The positive string matches are not enough to prove external activity indexing because the deployed JSON has zero records marked `external: true`; those words also appear in normal Hugo content.

## Diagnosis

The issue was index generation, not the `/search/` frontend and not browser cache.

The previous external-activity logic was added to:

- `layouts/_default/layouts_defaultindex.json.json`

But Hugo/PaperMod's home JSON lookup was still using:

- `themes/PaperMod/layouts/_default/index.json`

Because the local override had the wrong filename, the deployed `/index.json` was generated from PaperMod's default template and only contained regular Hugo pages.

## Fix

Added a correctly named Hugo layout override:

- `layouts/_default/index.json`

This override:

- Keeps regular Hugo page records first.
- Preserves filtering for empty or whitespace-only page titles.
- Preserves redirect-stub filtering.
- Appends records from `.Site.Data.activity.external_updates.items`.
- Appends records from `.Site.Data.activity.curated_outputs.items`.
- Sets external `permalink` to `source_url`.
- Skips external records with empty title, empty URL, or URL not starting with `http://` or `https://`.
- Allows curated records with `http://`, `https://`, or root-relative `/` URLs.
- Includes searchable text from title, summary, source label, source platform, activity type, and language.

No cache-busting change was added because the live index itself did not contain external records. Browser cache can only explain stale reads after the generated index is correct; here the deployed generated index was missing the records.

## Sample External Records

No external records were confirmed in the deployed index because the deployed index has `external: true` count of 0.

The following records are present in local data and are expected to appear in `/index.json` after Hugo rebuilds with `layouts/_default/index.json`.

Note:

```json
{
  "title": "10ドルの偽AirPodsを分解したら、中国TWSエコシステムが見えた【Nico-Tech Shenzhenフィールドノート】",
  "permalink": "https://note.com/takasu/n/n1b8935b01237",
  "source_label": "note",
  "source_platform": "note",
  "activity_type": "external",
  "language": "ja",
  "external": true
}
```

YouTube:

```json
{
  "title": "I Took Apart $10 Fake AirPods — Inside China’s TWS Earbud Ecosystem",
  "permalink": "https://www.youtube.com/watch?v=xAotcCqOcug",
  "source_label": "Nico-Tech Shenzhen Field Notes EN",
  "source_platform": "youtube",
  "activity_type": "video",
  "language": "en",
  "external": true
}
```

Podcast:

```json
{
  "title": "#09 10ドルの偽AirPodsを分解したら、中国TWSエコシステムが見えた",
  "permalink": "https://podcasters.spotify.com/pod/show/masakazu-tks-takasu/episodes/09-10AirPodsTWS-e3l0mpl",
  "source_label": "Podcast",
  "source_platform": "podcast",
  "activity_type": "podcast",
  "language": "ja",
  "external": true
}
```

researchmap:

```json
{
  "title": "初期導入構成から長期価値への移行に着目した開発者向けハードウェアプラットフォームの実証分析",
  "permalink": "https://researchmap.jp/takasumasakazu/presentations/53357621",
  "source_label": "researchmap",
  "source_platform": "researchmap",
  "activity_type": "talk",
  "language": "ja",
  "external": true
}
```

## Files Changed

- `layouts/_default/index.json`
- `layouts/_default/layouts_defaultindex.json.json`
- `assets/js/fastsearch.js`
- `reports/search-external-activity-audit.md`
- `reports/search-index-debug.md`

## Inline Source Icons

External activity records now include `source_icon` in the search index when available from `data/activity/external_updates.json`. The current data has `source_icon` for all 149 external activity items, so no data regeneration was required.

Search result rendering now prepends a compact 16px inline icon before the title only when `source_icon` is present and renderable:

`[16px icon] Title »`

Records without `source_icon`, including normal internal Hugo pages, still render as:

`Title »`

Broken icon images are hidden with an inline `onerror` handler, keeping the title visible and avoiding broken-image chrome.

## Public Directory

`public/` remains unchanged. Hugo is not installed locally, so no local rebuild was run.
