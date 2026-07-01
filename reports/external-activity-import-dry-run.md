# External Activity Import Dry Run

Generated: `2026-07-01T05:44:40.007296+00:00`

- mode: `dry-run`
- config used: `tools\activity_sources.example.json`
- proposed output path: `data\activity\external_updates.json`
- JSON written: `no`

This run does not modify existing content posts, metadata, `public/`, homepage, navigation, config, templates, or GitHub Actions.

## Source Results

| source_id | feed_or_site_url | platform | activity_type | language | status | items | issues |
| --- | --- | --- | --- | --- | --- | ---: | --- |
| youtube_ja | https://www.youtube.com/feeds/videos.xml?playlist_id=PLvhFXFu5H1DNJzI4HDEtX6dxsQsU01jmo | youtube | video | ja | failed | 0 | HTTP error for youtube_ja: 404 Not Found |
| youtube_en | https://www.youtube.com/feeds/videos.xml?playlist_id=PLvhFXFu5H1DNW74Y6kD4h5Uh0CCAy_EtU | youtube | video | en | failed | 0 | HTTP error for youtube_en: 404 Not Found |
| youtube_talks | https://www.youtube.com/feeds/videos.xml?playlist_id=PLvhFXFu5H1DONMcAltBRgYqRJn_bPxFnu | youtube | talk | mixed | failed | 0 | HTTP error for youtube_talks: 404 Not Found |
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

## Counts By Activity Type

- `book`: 6
- `external`: 76
- `paper`: 7
- `podcast`: 9
- `research`: 13
- `talk`: 9

## Counts By Language

- `en`: 14
- `ja`: 105
- `mixed`: 1

## Duplicate URL Warnings

- No duplicate normalized IDs or source URLs found.

Recommendation for future `/updates/` display: no duplicate URL handling is needed for this run.

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
    "image": "",
    "language": "ja",
    "topics": [],
    "featured": false,
    "source_id": "note_main",
    "external_id": "naf4b628e3aef",
    "imported_at": "2026-07-01T05:44:22.727445+00:00",
    "source_label": "note",
    "source_icon": "https://note.com/favicon.ico"
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
    "imported_at": "2026-07-01T05:44:22.727445+00:00",
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
    "image": "",
    "language": "ja",
    "topics": [],
    "featured": false,
    "source_id": "note_main",
    "external_id": "n1b8935b01237",
    "imported_at": "2026-07-01T05:44:22.727445+00:00",
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
    "image": "",
    "language": "en",
    "topics": [],
    "featured": false,
    "source_id": "medium_main",
    "external_id": "66e7ed494295",
    "imported_at": "2026-07-01T05:44:22.727445+00:00",
    "source_label": "Medium",
    "source_icon": "https://medium.com/favicon.ico"
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
    "imported_at": "2026-07-01T05:44:22.727445+00:00",
    "source_label": "Podcast",
    "source_icon": "https://open.spotify.com/favicon.ico"
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
    "imported_at": "2026-07-01T05:44:22.727445+00:00",
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
    "image": "",
    "language": "en",
    "topics": [],
    "featured": false,
    "source_id": "medium_main",
    "external_id": "8c3d093fdd7f",
    "imported_at": "2026-07-01T05:44:22.727445+00:00",
    "source_label": "Medium",
    "source_icon": "https://medium.com/favicon.ico"
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
    "imported_at": "2026-07-01T05:44:22.727445+00:00",
    "source_label": "note",
    "source_icon": "https://note.com/favicon.ico"
  },
  {
    "id": "medium:32ab9a149fbf",
    "activity_type": "external",
    "source_platform": "medium",
    "title": "From a $1 Made-in-India Calculator to a Chinese 4-bit CPU",
    "date": "2026-06-07T09:02:25+00:00",
    "source_url": "https://medium.com/shenzhen-high-tour-by-makers/from-a-1-made-in-india-calculator-to-a-chinese-4-bit-cpu-32ab9a149fbf",
    "canonical_url": "",
    "summary": "Chip decap in Shenzhen, low-cost electronics, and what “Made in” really means I gave the opening talk on Day 1 at Teardown 2026 . The talk was not only about opening products. It was about what teardown can reveal about the real structure of hardware manufacturing: where design happens, where components come from, how supply chains are connected, and how much of the story is hidden behind a simple “Made in” label. O...",
    "image": "",
    "language": "en",
    "topics": [],
    "featured": false,
    "source_id": "medium_main",
    "external_id": "32ab9a149fbf",
    "imported_at": "2026-07-01T05:44:22.727445+00:00",
    "source_label": "Medium",
    "source_icon": "https://medium.com/favicon.ico"
  },
  {
    "id": "podcast:bd870c5e-e782-4a64-80a9-5a9a75522be2",
    "activity_type": "podcast",
    "source_platform": "podcast",
    "title": "#08 インド製100円電卓をDecapしたら、中国製4ビットCPUが見えてきた Nico-Tech深圳フィールドノート",
    "date": "2026-06-07T02:09:00+00:00",
    "source_url": "https://podcasters.spotify.com/pod/show/masakazu-tks-takasu/episodes/08-100Decap4CPU-Nico-Tech-e3kedvc",
    "canonical_url": "",
    "summary": "インド・チェンナイの雑貨屋で買った、Made in India表記の100円台の電卓を分解し、さらに深圳のチップDecap業者に依頼して、黒いエポキシの下にあるチップの中まで見た話です。 以前の記事では、ホテルで分解した基板から「Made in Indiaの中に深圳の設計重力が見えるのではないか」と書きました。今回はその続きとして、Techanalyeさんの分析とチップDecapによって、基板のさらに下、シリコンのレイヤーまで見ています。そこにあったのは、中国SiLian MicroのSC2118系と見られる4ビットCPUでした。 この話は、2026年の分解・リバースエンジニアリング系イベント Teardown 2026 で、僕が初日のキーノートとして話す内容にもつながっています。安い電卓ひとつから、インドの製造、中国の低価格半導体、深圳のDecapサービス、日本の電卓産業史、そして「Made in」の意味までが見えてくる。今...",
    "image": "",
    "language": "ja",
    "topics": [],
    "featured": false,
    "source_id": "podcast_main",
    "external_id": "bd870c5e-e782-4a64-80a9-5a9a75522be2",
    "imported_at": "2026-07-01T05:44:22.727445+00:00",
    "source_label": "Podcast",
    "source_icon": "https://open.spotify.com/favicon.ico"
  }
]
```

## Safe To Run `--write` Next?

No.
- Some sources failed: youtube_ja, youtube_en, youtube_talks

## Recommended Next Step

Review this dry-run report. If the counts, sample records, and duplicate URL warnings are acceptable, run `tools/import_external_activity.py --write` in a later step to create `data/activity/external_updates.json`.
