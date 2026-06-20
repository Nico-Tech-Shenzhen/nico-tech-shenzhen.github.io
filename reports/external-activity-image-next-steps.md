# External Activity Image Next Steps

This is an audit only. Do not fetch article body pages or backfill thumbnails in this task.

## Safe Direct Thumbnail Sources

- YouTube RSS: use `media:thumbnail` from feed entries. This is the safest first implementation because the thumbnail is provided in the feed payload.
- Medium RSS: inspect feed-level image fields already present in RSS item content/metadata. Prefer direct feed-provided image URLs; do not crawl article pages.
- note RSS: use image data only when the feed/list response exposes a thumbnail or enclosure directly. Avoid scraping note article bodies.
- DG Lab RSS: use feed-provided enclosure/media/OG-like fields if present in the author feed. Do not fetch individual article pages.
- JST author/list page: may expose list thumbnails on the author/list page, but importer support should parse only the listing already used for discovery. Avoid article body fetches.

## Sources That Should Stay Text-Only For Now

- researchmap: keep text-only unless a stable, explicit thumbnail field exists in the profile data being parsed. Publication and presentation records are primarily bibliographic.
- Podcast: keep text-only unless the existing podcast feed exposes episode or show artwork directly and licensing/ownership is clear.
- Curated outputs: keep text-only until each item has an intentional image field or local asset.

## Later Importer Changes

- Add an optional `image` extraction step per source in `tools/import_external_activity.py`.
- Preserve the current empty string behavior when no safe direct thumbnail exists.
- Normalize image URLs to absolute URLs and reject data URIs, tracking pixels, and non-image responses.
- Keep `source_icon` separate from content thumbnails.
- Add a dry-run report that counts image coverage by `source_id` and lists sample URLs without downloading article bodies.
- Add tests or fixture checks for YouTube `media:thumbnail`, Medium/note/DG Lab feed image fields, and missing-image fallbacks.

## Non-Goals

- Do not fetch article body pages.
- Do not download or cache remote images.
- Do not infer thumbnails from Open Graph pages in this pass.
