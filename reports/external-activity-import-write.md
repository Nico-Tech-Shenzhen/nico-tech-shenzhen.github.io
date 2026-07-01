# External Activity Import Write

Generated: `2026-07-01T09:36:23.436559+00:00`

- mode: `write`
- config used: `tools\activity_sources.example.json`
- output path: `data\activity\external_updates.json`
- JSON written: `yes`

This run does not modify existing content posts, metadata, `public/`, homepage, navigation, config, templates, or GitHub Actions.

## Source Results

| source_id | feed_or_site_url | platform | activity_type | language | status | items | issues |
| --- | --- | --- | --- | --- | --- | ---: | --- |
| youtube_ja | https://www.youtube.com/feeds/videos.xml?playlist_id=PLvhFXFu5H1DNJzI4HDEtX6dxsQsU01jmo | youtube | video | ja | tested | 12 |  |
| youtube_en | https://www.youtube.com/feeds/videos.xml?playlist_id=PLvhFXFu5H1DNW74Y6kD4h5Uh0CCAy_EtU | youtube | video | en | tested | 4 |  |
| youtube_talks | https://www.youtube.com/feeds/videos.xml?playlist_id=PLvhFXFu5H1DONMcAltBRgYqRJn_bPxFnu | youtube | talk | mixed | tested | 13 |  |
| podcast_main | https://anchor.fm/s/10fd96ec0/podcast/rss | podcast | podcast | ja | tested | 9 |  |
| medium_main | https://medium.com/feed/shenzhen-high-tour-by-makers | medium | external | ja | tested | 10 |  |
| note_main | https://note.com/takasu/rss | note | external | ja | tested | 25 |  |
| dglab_main | https://media.dglab.com/author/masakazu-takasu/feed/ | dglab | external | ja | tested | 6 |  |
| jst_spc_takasu | https://spap.jst.go.jp/china/experiences/writers/takasu_06.html | jst_spc | external | ja | tested | 35 |  |
| researchmap_takasu | https://researchmap.jp/takasumasakazu | researchmap | research | mixed | tested | 35 |  |

## Counts By Source

- `dglab_main`: 6
- `jst_spc_takasu`: 35
- `medium_main`: 10
- `note_main`: 25
- `podcast_main`: 9
- `researchmap_takasu`: 35
- `youtube_en`: 4
- `youtube_ja`: 12
- `youtube_talks`: 13

## Counts By Activity Type

- `book`: 6
- `external`: 76
- `paper`: 7
- `podcast`: 9
- `research`: 13
- `talk`: 22
- `video`: 16

## Counts By Language

- `en`: 18
- `ja`: 129
- `mixed`: 2

## Duplicate URL Warnings

- Duplicate source URL `https://www.youtube.com/watch?v=ONTOW8gMeQ4` in `youtube_ja` and `youtube_en`.
- Duplicate source URL `https://www.youtube.com/watch?v=jV2kn8LlUZk` in `youtube_ja` and `youtube_en`.
- Duplicate source URL `https://www.youtube.com/watch?v=u-fWQ2WNavk` in `youtube_ja` and `youtube_talks`.

Recommendation for future `/updates/` display: hide duplicate source URLs by default and show the newest or preferred-language variant, while retaining both records in data for language/source-specific views.

## Sample Normalized Records

```json
[
  {
    "id": "note:naf4b628e3aef",
    "activity_type": "external",
    "source_platform": "note",
    "title": "200円のUSBケーブルを35円で買うときに見えてくる、深圳のサプライチェーン　【Nico-Tech Shenzhenフィールドノート】",
    "date": "2026-07-01T11:17:35+09:00",
    "source_url": "https://note.com/takasu/n/naf4b628e3aef",
    "canonical_url": "",
    "summary": "",
    "image": "https://assets.st-note.com/production/uploads/images/290404412/rectangle_large_type_2_d0293da7884a17cbf587ba3c2f02d5ce.jpeg?width=800",
    "language": "ja",
    "topics": [],
    "featured": false,
    "source_id": "note_main",
    "external_id": "naf4b628e3aef",
    "imported_at": "2026-07-01T09:35:58.977762+00:00",
    "source_label": "note",
    "source_icon": "https://note.com/favicon.ico"
  },
  {
    "id": "medium:9caa5d0dfd65",
    "activity_type": "external",
    "source_platform": "medium",
    "title": "What a 35-Cent USB-C Cable Reveals About Shenzhen’s Supply Chain",
    "date": "2026-07-01T09:19:22+00:00",
    "source_url": "https://medium.com/shenzhen-high-tour-by-makers/what-a-35-cent-usb-c-cable-reveals-about-shenzhens-supply-chain-9caa5d0dfd65",
    "canonical_url": "",
    "summary": "Small products often explain Shenzhen better than big slogans. A short USB-C to USB-C cable can be surprisingly useful. The type I looked at is a small strap-style cable. You can attach it to a phone, a bag, or a small device, and use it when you need to charge something outside. It is not a special product. You may find something similar in a 100-yen shop in Japan, or on Chinese e-commerce platforms for around 200...",
    "image": "https://cdn-images-1.medium.com/max/1024/1*_t8_gUAs0HDXyAOcQ6mm1g.jpeg",
    "language": "en",
    "topics": [],
    "featured": false,
    "source_id": "medium_main",
    "external_id": "9caa5d0dfd65",
    "imported_at": "2026-07-01T09:35:58.977762+00:00",
    "source_label": "Medium",
    "source_icon": "https://medium.com/favicon.ico"
  },
  {
    "id": "dglab:2026-06-29-dexmal-01",
    "activity_type": "external",
    "source_platform": "dglab",
    "title": "まずAI、次いでロボット　データ共有プラットフォームからロボットを開発する中国DEXMAL",
    "date": "2026-06-29T02:23:36+00:00",
    "source_url": "https://media.dglab.com/2026/06/29-dexmal-01",
    "canonical_url": "",
    "summary": "2026年4月、北京にあるDEXMAL（原力霊機）を訪問し、ジェネラルマネージャーのエミリー・チェン氏に話を聞いた。 DEXMALは、フィジカル AI、あるいはエンボディドAIと呼ばれる分野で急速に注目を集めているス... The post まずAI、次いでロボット データ共有プラットフォームからロボットを開発する中国DEXMAL first appeared on DG Lab Haus .",
    "image": "",
    "language": "ja",
    "topics": [],
    "featured": false,
    "source_id": "dglab_main",
    "external_id": "2026-06-29-dexmal-01",
    "imported_at": "2026-07-01T09:35:58.977762+00:00",
    "source_label": "DG Lab Haus",
    "source_icon": "https://media.dglab.com/favicon.ico"
  },
  {
    "id": "note:n1b8935b01237",
    "activity_type": "external",
    "source_platform": "note",
    "title": "10ドルの偽AirPodsを分解したら、中国TWSエコシステムが見えた【Nico-Tech Shenzhenフィールドノート】",
    "date": "2026-06-19T21:05:42+09:00",
    "source_url": "https://note.com/takasu/n/n1b8935b01237",
    "canonical_url": "",
    "summary": "深圳で買った、67元の「華強北 AirPods」を分解しました。 続きをみる",
    "image": "https://assets.st-note.com/production/uploads/images/286882119/rectangle_large_type_2_f519822ec112e5abb68bbe55fceaa0cf.png?width=800",
    "language": "ja",
    "topics": [],
    "featured": false,
    "source_id": "note_main",
    "external_id": "n1b8935b01237",
    "imported_at": "2026-07-01T09:35:58.977762+00:00",
    "source_label": "note",
    "source_icon": "https://note.com/favicon.ico"
  },
  {
    "id": "medium:66e7ed494295",
    "activity_type": "external",
    "source_platform": "medium",
    "title": "What $10 Fake AirPods Reveal About China’s Semiconductor Ecosystem",
    "date": "2026-06-19T12:41:58+00:00",
    "source_url": "https://medium.com/shenzhen-high-tour-by-makers/what-10-fake-airpods-reveal-about-chinas-semiconductor-ecosystem-66e7ed494295",
    "canonical_url": "",
    "summary": "A field note from Shenzhen: low-cost TWS earbuds, chip decap services, and the supply chains behind “fake” hardware I bought a pair of “Huaqiangbei AirPods” on Taobao for 67 RMB — about 10 USD at the time. They are clearly not genuine Apple AirPods. The packaging, the pairing screen, and the overall experience are designed to look familiar, but the product itself is a completely different piece of hardware. That is...",
    "image": "https://cdn-images-1.medium.com/max/1024/1*8KIJ3FyahjHrllkj-QhyaA.jpeg",
    "language": "en",
    "topics": [],
    "featured": false,
    "source_id": "medium_main",
    "external_id": "66e7ed494295",
    "imported_at": "2026-07-01T09:35:58.977762+00:00",
    "source_label": "Medium",
    "source_icon": "https://medium.com/favicon.ico"
  },
  {
    "id": "youtube:en:xAotcCqOcug",
    "activity_type": "video",
    "source_platform": "youtube",
    "title": "I Took Apart $10 Fake AirPods — Inside China’s TWS Earbud Ecosystem",
    "date": "2026-06-19T12:19:06+00:00",
    "source_url": "https://www.youtube.com/watch?v=xAotcCqOcug",
    "canonical_url": "",
    "summary": "In this episode of Nico-Tech Shenzhen Field Notes, I take apart a pair of $10 “Huaqiangbei AirPods” bought in Shenzhen and look at what they reveal about China’s low-cost TWS earbud and semiconductor ecosystem. These fake AirPods are clearly not genuine Apple products. But once opened, they are not just “bad copies” either. Inside, we can see cost-optimized engineering: a highly integrated Bluetooth audio SoC, simpl...",
    "image": "https://i1.ytimg.com/vi/xAotcCqOcug/hqdefault.jpg",
    "language": "en",
    "topics": [],
    "featured": false,
    "source_id": "youtube_en",
    "external_id": "xAotcCqOcug",
    "imported_at": "2026-07-01T09:35:58.977762+00:00",
    "source_label": "Nico-Tech Shenzhen Field Notes EN",
    "source_icon": "https://www.youtube.com/favicon.ico"
  },
  {
    "id": "podcast:d526da0b-fef3-4b2f-91e3-ad9440eb444e",
    "activity_type": "podcast",
    "source_platform": "podcast",
    "title": "#09 10ドルの偽AirPodsを分解したら、中国TWSエコシステムが見えた",
    "date": "2026-06-19T11:41:46+00:00",
    "source_url": "https://podcasters.spotify.com/pod/show/masakazu-tks-takasu/episodes/09-10AirPodsTWS-e3l0mpl",
    "canonical_url": "",
    "summary": "今回はTeardown 2026プレビュー特別編です。 深圳で購入した67元、約10ドルの「華強北 AirPods」を分解し、その中に見える中国TWSイヤホン産業のエコシステム、SoC、基板設計、Decap業者、そしてTeardown 2026で話す予定の内容を紹介します。 本物のAirPodsは片側だけで多数のチップやセンサーを使った高機能な製品ですが、今回分解した偽AirPodsは、メインSoC、タッチセンサー、MEMSマイク、クロックまわりなど、わずかなICで「それっぽい体験」を作っています。 単なる雑なコピーに見える製品でも、中を見ていくと、左右共通基板によるコスト削減、DFM、Jieli / Bluetrum系のTWS SoC、マーキングを消されたチップ、Taobaoで頼めるDecap業者、そして中国の分解コミュニティまで、安価なTWSイヤホンを支える独自の生態系が見えてきます。 後半では、インド製電卓のDecapか...",
    "image": "",
    "language": "ja",
    "topics": [],
    "featured": false,
    "source_id": "podcast_main",
    "external_id": "d526da0b-fef3-4b2f-91e3-ad9440eb444e",
    "imported_at": "2026-07-01T09:35:58.977762+00:00",
    "source_label": "Podcast",
    "source_icon": "https://open.spotify.com/favicon.ico"
  },
  {
    "id": "youtube:ja:UVJQNMm7wJk",
    "activity_type": "video",
    "source_platform": "youtube",
    "title": "第9回：10ドルの偽AirPodsを分解したら、中国TWSエコシステムが見えた｜Teardown 2026プレビュー",
    "date": "2026-06-19T11:25:49+00:00",
    "source_url": "https://www.youtube.com/watch?v=UVJQNMm7wJk",
    "canonical_url": "",
    "summary": "10ドル前後で売られている「華強北 AirPods」を分解し、その中に見える中国TWSイヤホン産業のエコシステム、SoC、基板設計、Decap業者、そしてTeardown 2026で話す内容のプレビューを紹介します。 偽物AirPodsは、もちろん本物のAirPodsとはまったく違います。 しかし中を見てみると、単なる雑なコピーではなく、安価なSoC、左右共通基板、部品点数削減、マーキングを消されたチップ、Taobaoで頼めるDecap業者など、中国のハードウェア産業らしい工夫と生態系が見えてきます。 今回は、深圳で購入した67元の偽AirPodsを分解し、Jieli / Bluetrum系のTWSチップ、System in Package、チップDecap、安価なTWS市場、そしてTeardown 2026でのオープニングトークにつながる話をします。 ▼ Chapters 00:00 オープニング：Teardown 2026...",
    "image": "https://i2.ytimg.com/vi/UVJQNMm7wJk/hqdefault.jpg",
    "language": "ja",
    "topics": [],
    "featured": false,
    "source_id": "youtube_ja",
    "external_id": "UVJQNMm7wJk",
    "imported_at": "2026-07-01T09:35:58.977762+00:00",
    "source_label": "Nico-Tech Shenzhen Field Notes JP",
    "source_icon": "https://www.youtube.com/favicon.ico"
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
    "image": "https://assets.st-note.com/production/uploads/images/285867934/rectangle_large_type_2_0f15d111a5537bd643ed5c084264cc35.jpeg?width=800",
    "language": "ja",
    "topics": [],
    "featured": false,
    "source_id": "note_main",
    "external_id": "nd01852684b73",
    "imported_at": "2026-07-01T09:35:58.977762+00:00",
    "source_label": "note",
    "source_icon": "https://note.com/favicon.ico"
  },
  {
    "id": "medium:8c3d093fdd7f",
    "activity_type": "external",
    "source_platform": "medium",
    "title": "Reading The Hardware Hacker in the Age of AI",
    "date": "2026-06-16T02:05:35+00:00",
    "source_url": "https://medium.com/shenzhen-high-tour-by-makers/reading-the-hardware-hacker-in-the-age-of-ai-8c3d093fdd7f",
    "canonical_url": "",
    "summary": "Where Does Your Curiosity Come From? I am very happy and honored that The Hardware Hacker by Andrew “bunnie” Huang has been chosen as a reading assignment for a seminar at the Interface Device Laboratory at Kanazawa University, where I currently belong. This book is personally meaningful to me because I am the Japanese translator of The Hardware Hacker . Seeing a book I translated become part of an academic discussi...",
    "image": "https://cdn-images-1.medium.com/max/747/1*wD5NtdMcxt_MgnPAWRNdmw.jpeg",
    "language": "en",
    "topics": [],
    "featured": false,
    "source_id": "medium_main",
    "external_id": "8c3d093fdd7f",
    "imported_at": "2026-07-01T09:35:58.977762+00:00",
    "source_label": "Medium",
    "source_icon": "https://medium.com/favicon.ico"
  }
]
```

## Write Safety

The write completed successfully. Duplicate source URLs were retained in JSON and should be handled by display logic.

## Recommended Next Step

Review `data/activity/external_updates.json` and the `/updates/` display before adding automation.
