# Activity Metadata Monthly Apply

Generated from the monthly-report-only apply run:

`python tools/apply_activity_metadata.py --apply --only-activity-type monthly_report --report reports/activity-metadata-monthly-apply.md`

## Summary

- total files considered by apply script: 408
- monthly_report files updated: 77
- skipped without writing: 331
- already-complete monthly_report sample files skipped: 5
- files requiring manual review and therefore not updated: 0 in this filtered monthly_report apply
- activity filter: `monthly_report`

## Metadata Added Summary

Only missing activity metadata fields were added:

- `activity_type: monthly_report`
- `source_platform`: inferred from the existing source/section
- `source_url: ""`
- `language`: inferred from cleaned article body text
- `topics`: inferred from title/body signals, normalized to use `events`
- `featured: false`

Existing `title`, `date`, `slug`, `aliases`, `cover`, `tags`, and body content were preserved. Existing complete metadata records, including the 5 monthly reports from the 15-file sample, were left unchanged.

No `podcast` topic was added by the monthly apply unless the article body specifically treats podcasting as a subject.

## Files Updated

- `content/archive/2026-2026-3-9f588165522f.md`
- `content/archive/2026-5-core2-m5stack-podcast-2026-44a929bb8a29.md`
- `content/archive/4-podcast-2026-23d2d68e6f91.md`
- `content/archive/m5stack-nt-2026-99821dceadc1.md`
- `content/archive/medium-github-pages-nico-tech-shenzhen-github-io-9ace82e922d5.md`
- `content/fabcross/2017-12-31_2018-1------------------defe8330825f.md`
- `content/fabcross/2018-02-28_------------8-----------------------2018-03--93f83a8d35c5.md`
- `content/fabcross/2018-03-31_-8----------------------------2018-04--a0c84b7adb85.md`
- `content/fabcross/2018-06-02_--------------NT-----------------------2018-06--93046e9dcce2.md`
- `content/fabcross/2018-07-04_7-------AkiParty------------------------2018-07--c5e7ff30319f.md`
- `content/fabcross/2018-10-02_-------------------------------------------------2018-10--1f572ea58a30.md`
- `content/fabcross/2018-11-01_------------------------------------------2018-11--f462fe4053e5.md`
- `content/fabcross/2018-11-29_2------------------------------------------2018-12--f349fb69b593.md`
- `content/fabcross/2019-01-31_2-14--JENESIS----------------------------------------------2019-0---551c611183e7.md`
- `content/fabcross/2019-04-30_------------------------------------------------------------2019-05--e2d248f83011.md`
- `content/fabcross/2019-07-01_8---------------------------------------------------------2019-07--62e72fa9aa5b.md`
- `content/fabcross/2019-10-10_-------------------------------------------------2019-10--3b38be5d5d86.md`
- `content/fabcross/2020-02-29_----------------------------------------------------------2020-03--a76f66b7ae1e.md`
- `content/fabcross/2020-03-31_--------------------------------------------2020-04--da633c3840df.md`
- `content/fabcross/2020-04-30_------------------------------------------2020-05--4f9a68ec6a3e.md`
- `content/fabcross/2020-11-30_---------------------------------------------------------2020-12--20517b1f0a24.md`
- `content/fabcross/2022-05-02_--------------------------------------------------------------2020-09--a16ff4d84229.md`
- `content/fabcross/2022-10-01_----------------------------------------2022-10--142578e61258.md`
- `content/fabcross/2023-05-07_--------------5-------------------2023-03--60a72e8d6468.md`
- `content/shenzhen/2018-01-31_2018-1-----------------------------------------------b48c0e9127d2.md`
- `content/shenzhen/2018-05-01_TAKASU---Nico-Tech-Shenzhen-Community-Monthly-news-May-2018-39f81c5de192.md`
- `content/shenzhen/2018-05-31_QuickStarter--More-inde-hardware-in-Kickstarter--TAKASU---Nico-Tech-Shenzhen-Community-Monthly-news-770231c2d57b.md`
- `content/shenzhen/2018-06-30_Monthly-News-July-2018-Amazing-Maker-Faire-Prague-and-Finally-come-to-AKIPARTY-Tokyo-fd45c8ae8bce.md`
- `content/shenzhen/2018-08-31_9-7---Xiaomi------------------------------------------------2018-09--bbd6b8c00cd.md`
- `content/shenzhen/2018-08-31_See-you-in-Maker-Faire-New-York---TAKASU---Nico-Tech-Shenzhen-Community-Monthly-news-Sep-2018-7a41d72ed766.md`
- `content/shenzhen/2018-11-30_Meet-again-Mitch-in-Shenzhen-TAKASU---Nico-Tech-Shenzhen-Community-Monthly-news-Dec-2018-e182dabb9bc7.md`
- `content/shenzhen/2018-12-31_See-you-in-CES--TAKASU---Nico-Tech-Shenzhen-Community-Monthly-news-Jan-2019-8ab8a36ce1ae.md`
- `content/shenzhen/2019-02-28_3-19----------------------------------------------------2019-03--f4bd9b5bfe17.md`
- `content/shenzhen/2019-04-01_----------------------------------------------2019-04--dc969a155e3.md`
- `content/shenzhen/2019-04-30_See-you-in-Maker-Faire-Bay-Area--TAKASU---Nico-Tech-Shenzhen-Community-Monthly-news-May-2019-34438463d948.md`
- `content/shenzhen/2019-07-31_Welcome-to-Maker-Faire-Tokyo-and-AkiParty-Japan--Monthly-report-2019-Aug-91315e885301.md`
- `content/shenzhen/2019-08-31_-----------10---------------------------------------------------2019-09--a07cf46bf928.md`
- `content/shenzhen/2019-10-31_--------------------------------------------------------------2019-11--a2a2b111475c.md`
- `content/shenzhen/2019-12-01_See-you-in-CES2020-US-and-BETT-2020-UK--TAKASU---Nico-Tech-Shenzhen-Community-Monthly-news-Dec-2019-4f3232e2d694.md`
- `content/shenzhen/2020-02-29_See-you-in-NY-and-Singapore--Monthly-Report-2020-March-eea8e268ac80.md`
- `content/shenzhen/2020-03-31_What-we-should-do-now--TAKASU---Nico-Tech-Shenzhen-Community-Monthly-news-March-2020-1f30405516c.md`
- `content/shenzhen/2020-05-01_Hope-to-back-to-Shenzhen--TAKASU---Nico-Tech-Shenzhen-Community-Monthly-news-May-2020-a6fee9aea704.md`
- `content/shenzhen/2020-05-31_Still-work-from-home-in-Japan--TAKASU---Nico-Tech-Shenzhen-Community-Monthly-news-May-2020-478dd3712281.md`
- `content/shenzhen/2020-07-31_HOPE-2020-Berlin-and-COSCUP-2020-Taipei-TAKASU---Nico-Tech-Shenzhen-Community-Monthly-news-Aug-2020-c4a602bcfcf1.md`
- `content/shenzhen/2021-01-31_Happy-CNY--I-m-still-in-Shenzhen--Feb-2021-monthly-report-fa6a18f9a3cb.md`
- `content/shenzhen/2023-01-04_-----------------2023-01--64b46033571d.md`
- `content/teardown/2018-07-29_8-4-AkiParty-8-5-----------------------------------2018-08--7cd459c0b626.md`
- `content/teardown/2018-12-31_--------------------2019-01--463ec61427c0.md`
- `content/teardown/2019-12-01_----WIRED-Audi------------------------2------------------------------------2019-12--2fac70a7a816.md`
- `content/teardown/2020-01-04_1-31-------------------------------------------------------------2020-01--f9b0a014c1b1.md`
- `content/teardown/2020-05-31_JENESIS----------6-13------------------------------------2020-06--84ef3ed1da2.md`
- `content/teardown/2020-06-30_-----------------------------------------------------2020-07--d27fd761928d.md`
- `content/teardown/2020-10-01_----------------------------------------------2020-10--9608ea34f437.md`
- `content/teardown/2020-11-01_11----------------Tech-------------------------------------2020-11--11fc4fac6367.md`
- `content/teardown/2021-03-01_----------------------------------------2021-03--acb955b20e7d.md`
- `content/teardown/2021-03-01_2-----------------------------------------2021-02--3d2c64afb866.md`
- `content/teardown/2021-06-01_---------6--------------------------------2021-06--1d57c8c95164.md`
- `content/teardown/2022-05-02_---------------------------------------------------2022-03--f914813ab4d3.md`
- `content/teardown/2022-05-02_---GDP-----------------------------------2022-05--4154c6cdf308.md`
- `content/teardown/2022-05-02_1-4--Podcast----------------------2022-01--9937c1f8ad37.md`
- `content/teardown/2022-07-31_--JENESIS--AIWA-------------------------2022-08--8c2de3aecab1.md`
- `content/teardown/2022-12-01_-----------------2022-12--a70a699b27e3.md`
- `content/teardown/2023-05-07_--------------------5-1--Panasonic-5-5-----------M5Stack-------------------------2023-05--ff923636bdaa.md`
- `content/teardown/2023-05-31_---------------6-17-18----------------------------2023-06--9ab17a0d0d12.md`
- `content/teardown/2023-07-31_--------------------------8-19-------------------------------2023-08--c3940c28e4bd.md`
- `content/teardown/2023-09-01_--------17----Discode---------------------------------------2023-09--b56e17c8945c.md`
- `content/teardown/2023-09-30_10-14-15--------------------------------------2023-10--45c94c772698.md`
- `content/teardown/2023-11-30_--------------------------2023-12--4780c9efb68c.md`
- `content/teardown/2024-02-01_----------------------------------2024-02--a201ea575985.md`
- `content/teardown/2024-02-29_------------------------------------2024-03--f57a5167ec68.md`
- `content/teardown/2024-06-30_--M5Stack-------KANTAN-Play-core-------------------------------2024-07--deb2ec8ed0fd.md`
- `content/teardown/2024-08-31_9-20-------------------------------------------------------2024-09--3bf927d7ea4c.md`
- `content/teardown/2025-05-31_6-21-22-NT-----------------------2025-06--9984a810b697.md`
- `content/teardown/2025-07-01_--------------------------------2025-07--50677ad54ff7.md`
- `content/teardown/2025-10-01_---------------10-7----------------------------2025-10--53d34a56fd42.md`
- `content/teardown/2025-11-01_-----AI--------------------------------2025-11--7f6710f6eb29.md`
- `content/teardown/2025-12-01_----------------12-5-6-------------------------2025-12--5ecab5ad5bbc.md`

## Uncertainty

- No manual-review files were updated in this filtered apply.
- The remaining risk is topic granularity on monthly reports with broad link roundups; those can be refined later without changing the core monthly_report classification.
