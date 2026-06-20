# External Activity Feed Audit

Generated: `2026-06-20T00:02:15.472568+00:00`

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

| source_id | feed_url | platform | activity_type | language | status | items | issues |
| --- | --- | --- | --- | --- | --- | ---: | --- |
| youtube_ja | https://www.youtube.com/feeds/videos.xml?playlist_id=PLvhFXFu5H1DNJzI4HDEtX6dxsQsU01jmo | youtube | video | ja | tested | 12 |  |
| youtube_en | https://www.youtube.com/feeds/videos.xml?playlist_id=PLvhFXFu5H1DNW74Y6kD4h5Uh0CCAy_EtU | youtube | video | en | tested | 4 |  |
| podcast_main | https://anchor.fm/s/10fd96ec0/podcast/rss | podcast | podcast | ja | tested | 9 |  |
| medium_main | https://medium.com/feed/shenzhen-high-tour-by-makers | medium | external | ja | tested | 10 |  |
| note_main | https://note.com/takasu/rss | note | external | ja | tested | 25 |  |

## Sample Normalized Items

### youtube_ja

| dedup ID | activity_type | date | title | language | source_url |
| --- | --- | --- | --- | --- | --- |
| youtube:ja:UVJQNMm7wJk | video | 2026-06-19T11:25:49+00:00 | 第9回：10ドルの偽AirPodsを分解したら、中国TWSエコシステムが見えた｜Teardown 2026プレビュー | ja | https://www.youtube.com/watch?v=UVJQNMm7wJk |
| youtube:ja:2ZxE0nYgXe8 | video | 2026-06-07T01:59:01+00:00 | インド製100円電卓を分解＆チップDecapしたら、中国製4ビットCPUが見えてきた フィールドノート #08 | ja | https://www.youtube.com/watch?v=2ZxE0nYgXe8 |
| youtube:ja:ONTOW8gMeQ4 | video | 2026-05-24T12:35:08+00:00 | Inside Shenzhen UAV Expo 2026: Drone Parts, RTK, Anti-Drone Tech, and Meituan Delivery #NicoTech #02 | ja | https://www.youtube.com/watch?v=ONTOW8gMeQ4 |
| youtube:ja:hMKFGIl6o6o | video | 2026-05-24T12:14:51+00:00 | #07 #UAVEXPO 2026現地レポート：DJI一強の先に見えた「自分たちで作るドローン」の時代　 そして美団ドローン配送の進化 #NicoTech深圳フィールドノート | ja | https://www.youtube.com/watch?v=hMKFGIl6o6o |
| youtube:ja:jV2kn8LlUZk | video | 2026-05-19T07:38:17+00:00 | #Humanoid01  Robots Ran a Half Marathon in Beijing — What I Saw on the Ground | ja | https://www.youtube.com/watch?v=jV2kn8LlUZk |

### youtube_en

| dedup ID | activity_type | date | title | language | source_url |
| --- | --- | --- | --- | --- | --- |
| youtube:en:xAotcCqOcug | video | 2026-06-19T12:19:06+00:00 | I Took Apart $10 Fake AirPods — Inside China’s TWS Earbud Ecosystem | en | https://www.youtube.com/watch?v=xAotcCqOcug |
| youtube:en:iB4cfdz80yM | video | 2026-06-07T08:29:17+00:00 | I Decapped a Cheap “Made in India” Calculator — and Found a Chinese 4-bit CPU #03 #teardown2026 | en | https://www.youtube.com/watch?v=iB4cfdz80yM |
| youtube:en:ONTOW8gMeQ4 | video | 2026-05-24T12:35:08+00:00 | Inside Shenzhen UAV Expo 2026: Drone Parts, RTK, Anti-Drone Tech, and Meituan Delivery #NicoTech #02 | en | https://www.youtube.com/watch?v=ONTOW8gMeQ4 |
| youtube:en:jV2kn8LlUZk | video | 2026-05-19T07:38:17+00:00 | #Humanoid01  Robots Ran a Half Marathon in Beijing — What I Saw on the Ground | en | https://www.youtube.com/watch?v=jV2kn8LlUZk |

### podcast_main

| dedup ID | activity_type | date | title | language | source_url |
| --- | --- | --- | --- | --- | --- |
| podcast:d526da0b-fef3-4b2f-91e3-ad9440eb444e | podcast | 2026-06-19T11:41:46+00:00 | #09 10ドルの偽AirPodsを分解したら、中国TWSエコシステムが見えた | ja | https://podcasters.spotify.com/pod/show/masakazu-tks-takasu/episodes/09-10AirPodsTWS-e3l0mpl |
| podcast:bd870c5e-e782-4a64-80a9-5a9a75522be2 | podcast | 2026-06-07T02:09:00+00:00 | #08 インド製100円電卓をDecapしたら、中国製4ビットCPUが見えてきた Nico-Tech深圳フィールドノート | ja | https://podcasters.spotify.com/pod/show/masakazu-tks-takasu/episodes/08-100Decap4CPU-Nico-Tech-e3kedvc |
| podcast:910416a2-3ef7-4e50-a49f-89233f6d572a | podcast | 2026-05-24T12:37:04+00:00 | #07 UAVEXPO 2026現地レポート：DJI一強の先に見えた「自分たちで作るドローン」の時代　#UAVEXPO そして美団ドローン配送の進化 #NicoTech深圳フィールドノート | ja | https://podcasters.spotify.com/pod/show/masakazu-tks-takasu/episodes/07-UAVEXPO-2026DJI-UAVEXPO--NicoTech-e3jqpr2 |
| podcast:3767f9ca-0889-4425-8cc3-9779fdfcb2eb | podcast | 2026-05-19T07:29:25+00:00 | #06 人間とロボットが同じ道を走った日——北京ヒューマノイドロボットハーフマラソン現地レポート | ja | https://podcasters.spotify.com/pod/show/masakazu-tks-takasu/episodes/06-e3jj2ia |
| podcast:2d58b0c4-e32d-40f6-ac24-89e3c6eea89b | podcast | 2026-04-15T05:13:41+00:00 | #8 myActuatorは現場でどう見られているのか｜FAエンジニアとの対話で見えた使いどころ（FA Radioコラボ） | ja | https://podcasters.spotify.com/pod/show/masakazu-tks-takasu/episodes/8-myActuatorFAFA-Radio-e3hu98d |

### medium_main

| dedup ID | activity_type | date | title | language | source_url |
| --- | --- | --- | --- | --- | --- |
| medium:66e7ed494295 | external | 2026-06-19T12:41:58+00:00 | What $10 Fake AirPods Reveal About China’s Semiconductor Ecosystem | ja | https://medium.com/shenzhen-high-tour-by-makers/what-10-fake-airpods-reveal-about-chinas-semiconductor-ecosystem-66e7ed494295 |
| medium:8c3d093fdd7f | external | 2026-06-16T02:05:35+00:00 | Reading The Hardware Hacker in the Age of AI | ja | https://medium.com/shenzhen-high-tour-by-makers/reading-the-hardware-hacker-in-the-age-of-ai-8c3d093fdd7f |
| medium:32ab9a149fbf | external | 2026-06-07T09:02:25+00:00 | From a $1 Made-in-India Calculator to a Chinese 4-bit CPU | ja | https://medium.com/shenzhen-high-tour-by-makers/from-a-1-made-in-india-calculator-to-a-chinese-4-bit-cpu-32ab9a149fbf |
| medium:5f79ce45df89 | external | 2026-06-01T05:56:00+00:00 | From Shenzhen Drones to DIY Chips: What I Learned This Month Across China, Japan, and the Maker… | ja | https://medium.com/shenzhen-high-tour-by-makers/from-shenzhen-drones-to-diy-chips-what-i-learned-this-month-across-china-japan-and-the-maker-5f79ce45df89 |
| medium:0ea2164dab8d | external | 2026-05-24T12:54:13+00:00 | At Shenzhen UAV Expo, Drones Are Becoming Something You Build, Not Just Something You Buy | ja | https://medium.com/shenzhen-high-tour-by-makers/at-shenzhen-uav-expo-drones-are-becoming-something-you-build-not-just-something-you-buy-0ea2164dab8d |

### note_main

| dedup ID | activity_type | date | title | language | source_url |
| --- | --- | --- | --- | --- | --- |
| note:n1b8935b01237 | external | 2026-06-19T21:05:42+09:00 | 10ドルの偽AirPodsを分解したら、中国TWSエコシステムが見えた【Nico-Tech Shenzhenフィールドノート】 | ja | https://note.com/takasu/n/n1b8935b01237 |
| note:nd01852684b73 | external | 2026-06-16T10:42:07+09:00 | AI時代に #ハードウェアハッカー を読むとは -あなたの好奇心はどこから来るか- #NT金沢 | ja | https://note.com/takasu/n/nd01852684b73 |
| note:n29dfc14da1fd | external | 2026-06-07T10:54:17+09:00 | インド製100円電卓をチップDecapしたら、中国製4ビットCPUが見えてきた【フィールドノート #08】 | ja | https://note.com/takasu/n/n29dfc14da1fd |
| note:n8981a16df9c9 | external | 2026-05-24T21:10:49+09:00 | #10 深圳UAV EXPOで見えた、ドローンが「買うもの」から「作るもの」に戻る瞬間 そして美団ドローン配送の進化 | ja | https://note.com/takasu/n/n8981a16df9c9 |
| note:n1ef2117406a0 | external | 2026-05-19T16:15:55+09:00 | #09 人間とロボットが同じ道を走った日——北京ヒューマノイドロボットハーフマラソン現地レポート | ja | https://note.com/takasu/n/n1ef2117406a0 |

## Duplicate Warnings

- Duplicate source URL `https://www.youtube.com/watch?v=ONTOW8gMeQ4` in `youtube_ja` and `youtube_en`.
- Duplicate source URL `https://www.youtube.com/watch?v=jV2kn8LlUZk` in `youtube_ja` and `youtube_en`.

## Parsing Issues

- No parsing issues reported.

## Recommended Next Step

Review the normalized samples and duplicate warnings. If they look correct, the next step is a dry-run importer that proposes `data/activity/*.json` changes in a report before enabling persistent data output.
