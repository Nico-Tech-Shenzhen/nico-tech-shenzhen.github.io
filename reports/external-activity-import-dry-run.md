# External Activity Import Dry Run

Generated: `2026-06-20T00:06:59.628240+00:00`

- mode: `dry-run`
- config used: `tools\activity_sources.example.json`
- proposed output path: `data\activity\external_updates.json`
- JSON written: `no`

This run does not modify existing content posts, metadata, `public/`, homepage, navigation, config, templates, or GitHub Actions.

## Source Results

| source_id | feed_url | platform | activity_type | language | status | items | issues |
| --- | --- | --- | --- | --- | --- | ---: | --- |
| youtube_ja | https://www.youtube.com/feeds/videos.xml?playlist_id=PLvhFXFu5H1DNJzI4HDEtX6dxsQsU01jmo | youtube | video | ja | tested | 12 |  |
| youtube_en | https://www.youtube.com/feeds/videos.xml?playlist_id=PLvhFXFu5H1DNW74Y6kD4h5Uh0CCAy_EtU | youtube | video | en | tested | 4 |  |
| podcast_main | https://anchor.fm/s/10fd96ec0/podcast/rss | podcast | podcast | ja | tested | 9 |  |
| medium_main | https://medium.com/feed/shenzhen-high-tour-by-makers | medium | external | ja | tested | 10 |  |
| note_main | https://note.com/takasu/rss | note | external | ja | tested | 25 |  |

## Counts By Source

- `medium_main`: 10
- `note_main`: 25
- `podcast_main`: 9
- `youtube_en`: 4
- `youtube_ja`: 12

## Counts By Activity Type

- `external`: 35
- `podcast`: 9
- `video`: 16

## Counts By Language

- `en`: 4
- `ja`: 56

## Duplicate URL Warnings

- Duplicate source URL `https://www.youtube.com/watch?v=ONTOW8gMeQ4` in `youtube_ja` and `youtube_en`.
- Duplicate source URL `https://www.youtube.com/watch?v=jV2kn8LlUZk` in `youtube_ja` and `youtube_en`.

Recommendation for future `/updates/` display: hide duplicate source URLs by default and show the newest or preferred-language variant, while retaining both records in data for language/source-specific views.

## Sample Normalized Records

```json
[
  {
    "id": "note:n1b8935b01237",
    "activity_type": "external",
    "source_platform": "note",
    "title": "10ドルの偽AirPodsを分解したら、中国TWSエコシステムが見えた【Nico-Tech Shenzhenフィールドノート】",
    "date": "2026-06-19T21:05:42+09:00",
    "source_url": "https://note.com/takasu/n/n1b8935b01237",
    "canonical_url": "",
    "summary": "深圳で買った、67元の「華強北 AirPods」を分解しました。 続きをみる",
    "image": "",
    "language": "ja",
    "topics": [],
    "featured": false,
    "source_id": "note_main",
    "external_id": "n1b8935b01237",
    "imported_at": "2026-06-20T00:06:57.736546+00:00"
  },
  {
    "id": "medium:66e7ed494295",
    "activity_type": "external",
    "source_platform": "medium",
    "title": "What $10 Fake AirPods Reveal About China’s Semiconductor Ecosystem",
    "date": "2026-06-19T12:41:58+00:00",
    "source_url": "https://medium.com/shenzhen-high-tour-by-makers/what-10-fake-airpods-reveal-about-chinas-semiconductor-ecosystem-66e7ed494295",
    "canonical_url": "",
    "summary": "A field note from Shenzhen: low-cost TWS earbuds, chip decap services, and the supply chains behind “fake” hardware I bought a pair of “Huaqiangbei AirPods” on Taobao for 67 RMB — about 10 USD at the time. They are clearly not genuine Apple AirPods. The packaging, the pairing sc...",
    "image": "",
    "language": "ja",
    "topics": [],
    "featured": false,
    "source_id": "medium_main",
    "external_id": "66e7ed494295",
    "imported_at": "2026-06-20T00:06:57.736546+00:00"
  },
  {
    "id": "youtube:en:xAotcCqOcug",
    "activity_type": "video",
    "source_platform": "youtube",
    "title": "I Took Apart $10 Fake AirPods — Inside China’s TWS Earbud Ecosystem",
    "date": "2026-06-19T12:19:06+00:00",
    "source_url": "https://www.youtube.com/watch?v=xAotcCqOcug",
    "canonical_url": "",
    "summary": "",
    "image": "",
    "language": "en",
    "topics": [],
    "featured": false,
    "source_id": "youtube_en",
    "external_id": "xAotcCqOcug",
    "imported_at": "2026-06-20T00:06:57.736546+00:00"
  },
  {
    "id": "podcast:d526da0b-fef3-4b2f-91e3-ad9440eb444e",
    "activity_type": "podcast",
    "source_platform": "podcast",
    "title": "#09 10ドルの偽AirPodsを分解したら、中国TWSエコシステムが見えた",
    "date": "2026-06-19T11:41:46+00:00",
    "source_url": "https://podcasters.spotify.com/pod/show/masakazu-tks-takasu/episodes/09-10AirPodsTWS-e3l0mpl",
    "canonical_url": "",
    "summary": "今回はTeardown 2026プレビュー特別編です。 深圳で購入した67元、約10ドルの「華強北 AirPods」を分解し、その中に見える中国TWSイヤホン産業のエコシステム、SoC、基板設計、Decap業者、そしてTeardown 2026で話す予定の内容を紹介します。 本物のAirPodsは片側だけで多数のチップやセンサーを使った高機能な製品ですが、今回分解した偽AirPodsは、メインSoC、タッチセンサー、MEMSマイク、クロックまわりなど、わずかなICで「それっぽい体験」を作っています。 単なる雑なコピーに見える製品でも、中を見ていくと、左...",
    "image": "",
    "language": "ja",
    "topics": [],
    "featured": false,
    "source_id": "podcast_main",
    "external_id": "d526da0b-fef3-4b2f-91e3-ad9440eb444e",
    "imported_at": "2026-06-20T00:06:57.736546+00:00"
  },
  {
    "id": "youtube:ja:UVJQNMm7wJk",
    "activity_type": "video",
    "source_platform": "youtube",
    "title": "第9回：10ドルの偽AirPodsを分解したら、中国TWSエコシステムが見えた｜Teardown 2026プレビュー",
    "date": "2026-06-19T11:25:49+00:00",
    "source_url": "https://www.youtube.com/watch?v=UVJQNMm7wJk",
    "canonical_url": "",
    "summary": "",
    "image": "",
    "language": "ja",
    "topics": [],
    "featured": false,
    "source_id": "youtube_ja",
    "external_id": "UVJQNMm7wJk",
    "imported_at": "2026-06-20T00:06:57.736546+00:00"
  },
  {
    "id": "note:nd01852684b73",
    "activity_type": "external",
    "source_platform": "note",
    "title": "AI時代に #ハードウェアハッカー を読むとは -あなたの好奇心はどこから来るか- #NT金沢",
    "date": "2026-06-16T10:42:07+09:00",
    "source_url": "https://note.com/takasu/n/nd01852684b73",
    "canonical_url": "",
    "summary": "僕の所属している 金沢大学インターフェイスデバイス研究室 での輪講が「ハードウェア・ハッカー」（著：バニー・ファン、訳：高須正和、監訳：山形浩生）になった。自分の訳書がゼミの課題図書になるのはとてもうれしいし光栄。 ハードウェアハッカー～新しいモノをつくる破壊と創造の冒険 amzn.to 2,566円 (2026年06月16日 10:05時点詳しくはこちら) Amazon.co.jpで購入する 続きをみる",
    "image": "",
    "language": "ja",
    "topics": [],
    "featured": false,
    "source_id": "note_main",
    "external_id": "nd01852684b73",
    "imported_at": "2026-06-20T00:06:57.736546+00:00"
  },
  {
    "id": "medium:8c3d093fdd7f",
    "activity_type": "external",
    "source_platform": "medium",
    "title": "Reading The Hardware Hacker in the Age of AI",
    "date": "2026-06-16T02:05:35+00:00",
    "source_url": "https://medium.com/shenzhen-high-tour-by-makers/reading-the-hardware-hacker-in-the-age-of-ai-8c3d093fdd7f",
    "canonical_url": "",
    "summary": "Where Does Your Curiosity Come From? I am very happy and honored that The Hardware Hacker by Andrew “bunnie” Huang has been chosen as a reading assignment for a seminar at the Interface Device Laboratory at Kanazawa University, where I currently belong. This book is personally m...",
    "image": "",
    "language": "ja",
    "topics": [],
    "featured": false,
    "source_id": "medium_main",
    "external_id": "8c3d093fdd7f",
    "imported_at": "2026-06-20T00:06:57.736546+00:00"
  },
  {
    "id": "note:n29dfc14da1fd",
    "activity_type": "external",
    "source_platform": "note",
    "title": "インド製100円電卓をチップDecapしたら、中国製4ビットCPUが見えてきた【フィールドノート #08】",
    "date": "2026-06-07T10:54:17+09:00",
    "source_url": "https://note.com/takasu/n/n29dfc14da1fd",
    "canonical_url": "",
    "summary": "インド・チェンナイで買った、Made in India表記の100円台の電卓を分解し、さらに深圳のチップDecap業者に依頼して、黒いエポキシの下にあるチップの中まで見た話です。 以前の記事では、ホテルで分解した基板から「Made in Indiaの中に深圳の設計重力が見えるのではないか」と書きました。今回はその続きとして、Techanalyeさんの分析とチップDecapによって、基板のさらに下、シリコンのレイヤーまで見ています。そこにあったのは、中国SiLian MicroのSC2118系と見られる4ビットCPUでした。 続きをみる",
    "image": "",
    "language": "ja",
    "topics": [],
    "featured": false,
    "source_id": "note_main",
    "external_id": "n29dfc14da1fd",
    "imported_at": "2026-06-20T00:06:57.736546+00:00"
  },
  {
    "id": "medium:32ab9a149fbf",
    "activity_type": "external",
    "source_platform": "medium",
    "title": "From a $1 Made-in-India Calculator to a Chinese 4-bit CPU",
    "date": "2026-06-07T09:02:25+00:00",
    "source_url": "https://medium.com/shenzhen-high-tour-by-makers/from-a-1-made-in-india-calculator-to-a-chinese-4-bit-cpu-32ab9a149fbf",
    "canonical_url": "",
    "summary": "Chip decap in Shenzhen, low-cost electronics, and what “Made in” really means I gave the opening talk on Day 1 at Teardown 2026 . The talk was not only about opening products. It was about what teardown can reveal about the real structure of hardware manufacturing: where design...",
    "image": "",
    "language": "ja",
    "topics": [],
    "featured": false,
    "source_id": "medium_main",
    "external_id": "32ab9a149fbf",
    "imported_at": "2026-06-20T00:06:57.736546+00:00"
  },
  {
    "id": "youtube:en:iB4cfdz80yM",
    "activity_type": "video",
    "source_platform": "youtube",
    "title": "I Decapped a Cheap “Made in India” Calculator — and Found a Chinese 4-bit CPU #03 #teardown2026",
    "date": "2026-06-07T08:29:17+00:00",
    "source_url": "https://www.youtube.com/watch?v=iB4cfdz80yM",
    "canonical_url": "",
    "summary": "",
    "image": "",
    "language": "en",
    "topics": [],
    "featured": false,
    "source_id": "youtube_en",
    "external_id": "iB4cfdz80yM",
    "imported_at": "2026-06-20T00:06:57.736546+00:00"
  }
]
```

## Safe To Run `--write` Next?

Yes, with one caveat: duplicate source URLs should be accepted as known warnings or handled by display logic later. This importer will not remove duplicates yet.

## Recommended Next Step

Review this dry-run report. If the counts, sample records, and duplicate URL warnings are acceptable, run `tools/import_external_activity.py --write` in a later step to create `data/activity/external_updates.json`.
