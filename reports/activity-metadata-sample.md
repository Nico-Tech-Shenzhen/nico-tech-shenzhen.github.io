# Activity Metadata Sample

This report documents the Phase 1 sample metadata application. No files were moved, and no existing titles, dates, slugs, aliases, covers, or tags were changed.

## Summary

- Modified content files: 15
- Monthly reports: 5
- Normal Japanese posts: 3
- Normal English posts: 3
- Teardown posts: 2
- Talk posts: 1
- Book/publication announcement posts: 1
- Draft files touched: 0
- `public/` touched: no

## Modified Files

| file | old front matter summary | new metadata added | reason | uncertainty |
| --- | --- | --- | --- | --- |
| `content/teardown/2026-02-01_CES2026-2--------------------------2026-02--1d3242b26713.md` | title/date/slug/aliases/tags existed; tag was `monthly-report` | `activity_type: monthly_report`; `source_platform: medium`; `source_url: ""`; `language: ja`; `topics: ["community", "events", "shenzhen"]`; `featured: false` | Title and existing tag identify it as a monthly report. | Source URL is not present in front matter, so `source_url` remains empty. |
| `content/fabcross/2018-05-01_------------------------------------2018-05--a9009f67c3ae.md` | title/date/slug/aliases/tags/cover existed; tag was `monthly-report` | `activity_type: monthly_report`; `source_platform: fabcross`; `source_url: ""`; `language: ja`; `topics: ["community", "shenzhen"]`; `featured: false` | Fabcross section and monthly-report tag are high-confidence signals. | None beyond imported-source URL not recorded. |
| `content/fabcross/2019-07-31_------------------AkiParty---------------------------------------2019-08--816151511012.md` | title/date/slug/aliases/tags/cover existed; tag was `monthly-report` | `activity_type: monthly_report`; `source_platform: fabcross`; `source_url: ""`; `language: ja`; `topics: ["community", "events", "maker-faire", "shenzhen"]`; `featured: false` | Title and tag identify monthly report; title mentions Tokyo event and AkiParty. | None beyond imported-source URL not recorded. |
| `content/fabcross/2022-05-02_RCEP------------------------------------------------12f64bc3bffd.md` | title/date/slug/aliases/tags existed; tag was `monthly-report` | `activity_type: monthly_report`; `source_platform: fabcross`; `source_url: ""`; `language: ja`; `topics: ["community", "open-source", "shenzhen"]`; `featured: false` | Title and tag identify monthly report; title/body focus on community and open-source business use. | Topics are intentionally broad. |
| `content/teardown/2021-09-03_9-6-21-30---IT-------------------podcast---------------------2021-09--a04553077adc.md` | title/date/slug/aliases/tags/cover existed; tag was `monthly-report` | `activity_type: monthly_report`; `source_platform: medium`; `source_url: ""`; `language: ja`; `topics: ["community", "shenzhen"]`; `featured: false` | Existing tag and title identify monthly report; podcast remains future activity/source metadata rather than a topic here. | Source URL is not present in front matter. |
| `content/archive/2020-04-17_-------------aaafa0d2a435.md` | title/date/slug/aliases/cover existed; no tags | `activity_type: post`; `source_platform: medium`; `source_url: ""`; `language: ja`; `topics: ["book", "community"]`; `featured: false` | Japanese essay/post about reading books; no stronger activity type signal. | `book` is a topic here, not activity type. |
| `content/shenzhen/2023-06-25_ChatGPT-------------------------dd4331d1d234.md` | title/date/slug/aliases/cover existed; no tags | `activity_type: post`; `source_platform: medium`; `source_url: ""`; `language: ja`; `topics: ["ai", "writing"]`; `featured: false` | Japanese article about using ChatGPT for English writing. | None. |
| `content/archive/2025-02-09_---------AI-----------------------------OpenAI-Deepseek--AI-----------------------894bb0a506c5.md` | title/date/slug/aliases/cover existed; no tags | `activity_type: post`; `source_platform: medium`; `source_url: ""`; `language: ja`; `topics: ["ai", "open-source"]`; `featured: false` | Japanese article about OpenAI, Deepseek, and open-source AI. | None. |
| `content/archive/2018-01-23_TCDC-Thailand-Creative-and-Design-Centre--Fabcafe-X--Co-working--Library-4895748231cd.md` | title/date/slug/aliases/cover existed; no tags | `activity_type: post`; `source_platform: medium`; `source_url: ""`; `language: en`; `topics: ["design", "maker", "workspace"]`; `featured: false` | English field note about TCDC/Fabcafe/workspace. | None. |
| `content/archive/2013-10-28_Top-picks-at-the-Singapore-Biennale-7bd6a5e0df44.md` | title/date/slug/aliases/cover existed; no tags | `activity_type: post`; `source_platform: medium`; `source_url: ""`; `language: en`; `topics: ["art", "singapore"]`; `featured: false` | Short English post about Singapore Biennale. | Minimal body means topics are title-led. |
| `content/archive/2016-09-27_Notable-Maker-Mr--Higekita--His-DIY-3D-planetarium-is-unforgettable-project--f1be69cce10a.md` | title/date/slug/aliases/cover existed; no tags | `activity_type: post`; `source_platform: medium`; `source_url: ""`; `language: en`; `topics: ["diy", "maker"]`; `featured: false` | English maker profile/article. | None. |
| `content/teardown/2025-03-26_-----ISA----------------RISC-V-------0f3ec1085b2c.md` | title/date/slug/aliases/cover existed; no tags | `activity_type: post`; `source_platform: medium`; `source_url: ""`; `language: ja`; `topics: ["hardware", "open-source", "risc-v", "teardown"]`; `featured: false` | Teardown-section Japanese hardware/open ISA article. | `teardown` is included because of section placement, though the article is broader than physical teardown. |
| `content/teardown/2025-03-25_IoT---------------------------M5Stack--cd32050fb5c1.md` | title/date/slug/aliases/cover existed; no tags | `activity_type: post`; `source_platform: medium`; `source_url: ""`; `language: ja`; `topics: ["hardware", "iot", "m5stack", "teardown"]`; `featured: false` | Teardown-section Japanese M5Stack hardware article. | `teardown` is section-derived. |
| `content/shenzhen/2015-08-06_Talk-Asian-Maker-Faire-at-Maker-Faire-Tokyo-2015-649204dc2184.md` | title/date/slug/aliases existed; no tags | `activity_type: talk`; `source_platform: conference`; `source_url: ""`; `language: en`; `topics: ["maker-faire", "shenzhen", "talk"]`; `featured: false` | Title and body explicitly describe a talk at Maker Faire Tokyo. | No conference URL is recorded. |
| `content/shenzhen/2017-03-08_Published-book--Makers--ecosystem--reporting-innovation-in-Asia--Shenzhen-and-Singapore-359b360acbfe.md` | title/date/slug/aliases/cover existed; no tags | `activity_type: post`; `source_platform: medium`; `source_url: ""`; `language: en`; `topics: ["book", "maker", "shenzhen", "singapore"]`; `featured: false` | This is an article announcing the published book `Makers' ecosystem`, not the book object itself. | Dedicated book records/pages can model actual book objects later. |
