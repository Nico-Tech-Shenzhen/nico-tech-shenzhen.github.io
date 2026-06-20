# YouTube Description RSS Audit

Generated: `2026-06-20T09:31:00+00:00`

Scope: `youtube_ja`, `youtube_en`, and `youtube_talks` from `tools/activity_sources.example.json`.

This audit inspected only YouTube RSS/Atom playlist feeds. It did not fetch YouTube watch pages, did not use the YouTube API, and did not invent descriptions.

## Field Summary

| source_id | entries | title | link | summary | description | media:description | media_group / media_* | content |
| --- | ---: | --- | --- | --- | --- | --- | --- | --- |
| `youtube_ja` | 12 | present on entries | present as Atom alternate link | not present | not present as direct Atom field | 12 nodes, 11 non-empty | `media:group` contains `media:title`, `media:content`, `media:thumbnail`, `media:description`, `media:community` | not present |
| `youtube_en` | 4 | present on entries | present as Atom alternate link | not present | not present as direct Atom field | 4 nodes, 4 non-empty | `media:group` contains `media:title`, `media:content`, `media:thumbnail`, `media:description`, `media:community` | not present |
| `youtube_talks` | 13 | present on entries | present as Atom alternate link | not present | not present as direct Atom field | 13 nodes, 5 non-empty | `media:group` contains `media:title`, `media:content`, `media:thumbnail`, `media:description`, `media:community` | not present |

## Findings

- YouTube playlist RSS is Atom, not RSS `<item>` format.
- The useful description field is `media:group/media:description`.
- Atom `summary`, direct `description`, and Atom `content` were not exposed on sampled entries for these three playlist feeds.
- `youtube_en` does expose descriptions in RSS: all 4 current English playlist items have non-empty `media:description`.
- Some `youtube_talks` entries genuinely have empty `media:description`; those should remain empty rather than be fabricated.

## Sample Fields

### youtube_ja

Sampled first three entries.

| title | link | useful description field | media children |
| --- | --- | --- | --- |
| 第9回：10ドルの偽AirPodsを分解したら、中国TWSエコシステムが見えた｜Teardown 2026プレビュー | https://www.youtube.com/watch?v=UVJQNMm7wJk | non-empty `media:description` | title, content, thumbnail, description, community |
| インド製100円電卓を分解＆チップDecapしたら、中国製4ビットCPUが見えてきた フィールドノート #08 | https://www.youtube.com/watch?v=2ZxE0nYgXe8 | non-empty `media:description` | title, content, thumbnail, description, community |
| Inside Shenzhen UAV Expo 2026: Drone Parts, RTK, Anti-Drone Tech, and Meituan Delivery #NicoTech #02 | https://www.youtube.com/watch?v=ONTOW8gMeQ4 | non-empty `media:description` | title, content, thumbnail, description, community |

### youtube_en

Sampled first three entries.

| title | link | useful description field | media children |
| --- | --- | --- | --- |
| I Took Apart $10 Fake AirPods — Inside China’s TWS Earbud Ecosystem | https://www.youtube.com/watch?v=xAotcCqOcug | non-empty `media:description` | title, content, thumbnail, description, community |
| I Decapped a Cheap “Made in India” Calculator — and Found a Chinese 4-bit CPU #03 #teardown2026 | https://www.youtube.com/watch?v=iB4cfdz80yM | non-empty `media:description` | title, content, thumbnail, description, community |
| Inside Shenzhen UAV Expo 2026: Drone Parts, RTK, Anti-Drone Tech, and Meituan Delivery #NicoTech #02 | https://www.youtube.com/watch?v=ONTOW8gMeQ4 | non-empty `media:description` | title, content, thumbnail, description, community |

### youtube_talks

Sampled first three entries.

| title | link | useful description field | media children |
| --- | --- | --- | --- |
| WBS12 高須 stampfly オープンイノベーション | https://www.youtube.com/watch?v=WArYVtr-pzM | empty `media:description` | title, content, thumbnail, description, community |
| WBS6 アイデアを実際に作って売る方法　WBS06 深センの産業集積とハードウェアのマスイノベーション | https://www.youtube.com/watch?v=wSF9jA6tykM | empty `media:description` | title, content, thumbnail, description, community |
| WBS07 20260207 Heroad回 深圳の産業集積とハードウェアのマスイノベーション | https://www.youtube.com/watch?v=u-fWQ2WNavk | empty `media:description` | title, content, thumbnail, description, community |

## Importer Decision

Use the first non-empty normalized value in this order:

1. `media:description`
2. `summary`
3. `description`
4. `content` / `encoded`
5. empty string

Descriptions are stripped of HTML tags, entity-decoded, whitespace-collapsed, and capped at 420 characters before being written to `data/activity/external_updates.json`.
