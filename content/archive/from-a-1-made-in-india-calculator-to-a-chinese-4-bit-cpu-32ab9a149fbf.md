---
title: "From a $1 Made-in-India Calculator to a Chinese 4-bit CPU"
date: 2026-06-07T09:02:24+00:00
tags: ["teardown2026", "teardown", "decaps", "chipdecap"]
source: "https://medium.com/shenzhen-high-tour-by-makers/from-a-1-made-in-india-calculator-to-a-chinese-4-bit-cpu-32ab9a149fbf"
---

![](https://cdn-images-1.medium.com/max/1024/1*eku-OHoZQpgkzB8b-e0hgQ.png)

Chip decap in Shenzhen, low-cost electronics, and what “Made in” really meansI gave the opening talk on Day 1 at Teardown 2026.

The talk was not only about opening products. It was about what teardown can reveal about the real structure of hardware manufacturing: where design happens, where components come from, how supply chains are connected, and how much of the story is hidden behind a simple “Made in” label.

One of the stories I shared started with a very cheap calculator I bought in Chennai, India.

The box said Made in India.

![](https://cdn-images-1.medium.com/max/1024/1*Z0vHo9ltnOTHjUItq9qLhA.jpeg)

The price was roughly around one US dollar.

So I bought it, brought it back to my hotel room, and opened it.A simple calculator with a complicated storyInside the calculator was a very simple structure: a plastic case, a rubber keypad, an LCD, a button cell, one PCB, and a black epoxy chip-on-board package.

At first glance, it looked like an ordinary low-cost calculator. But the PCB layout, component choices, and overall design felt very familiar to me. It looked like something deeply connected to the Chinese low-cost electronics supply chain.

Later, with the help of Techanalye, we looked more closely at the calculator and compared it with similar products found in China. The calculator turned out to be part of a widely distributed CT-512 type product family, sold under multiple unclear or slightly different brands.

That is where the story became more interesting.

Was it Indian?
 Was it Chinese?
 Was it designed in one place and assembled in another?
 And what does Made in India actually mean in this case?

![](https://cdn-images-1.medium.com/max/1024/1*Fu2EQPoZieFV01eDcgKYGg.png)

The black epoxy was only the beginningThe most interesting part of the PCB was the black epoxy blob.

For many low-cost products, this is where a normal teardown stops. You can see the PCB. You can see the packaging. You can guess that there is a chip under the epoxy. But you cannot see the silicon itself.

In Shenzhen, however, stopping there is not always necessary.Chip decap is surprisingly accessible in ChinaOne of the things I wanted to introduce at [Teardown 2026](https://www.crowdsupply.com/teardown/portland-2026/long-talk/what-10-fake-airpods-and-a-30-chip-decap-reveal-about-chinas-semiconductors) is how accessible chip decap services can be in China.

![](https://cdn-images-1.medium.com/max/1024/1*A79abhknAkTWUavaZcPDQg.png)

In many countries, if you want to look inside a chip, it sounds like something that requires a university lab, an expensive failure analysis facility, or a corporate semiconductor team.

In Shenzhen, it can be much more practical.

You can find service providers online, talk to them directly, explain what you want, send the sample, and receive microscope photos a few days later.

For a simple chip like this calculator IC, the cost was around 150 RMB.

That price point matters.

![](https://cdn-images-1.medium.com/max/1024/1*f3L3dap8CNkNmVKMThVz5w.png)

It means chip decap is not only for large companies or formal research institutions. It can also become part of a maker, engineer, journalist, or independent researcher’s toolkit.Negotiating through Taobao and chatThe process was also straightforward.

I found a decap service provider through Taobao, contacted them via chat, explained that I wanted to open the chip and get microscope images, and sent the sample. After a few days, they sent back clear images of the silicon die.

![](https://cdn-images-1.medium.com/max/723/1*6H6ThAGhWifAIh6rm8f30g.png)

This is one of the unique strengths of the Shenzhen ecosystem.

It is not only that the services exist. It is that the distance between an idea and execution is short.

Need a PCB? Find a supplier.
 Need a component? Search the market.
 Need a case? Talk to a factory.
 Need to look inside a chip? Ask a decap service provider.

Each step may not be perfect or polished, but the path is open.What we found insideWith the decap images and Techanalye’s analysis, the chip appears to be a SiLian Micro SC2118-series calculator chip from China.

It is a 4-bit CPU that integrates ROM, RAM, keyboard scanning, and 7-segment display control.

![](https://cdn-images-1.medium.com/max/1024/1*kpTRLQqTdT5b3LqTB8ParQ.jpeg)

In other words, under the black epoxy of a very cheap calculator was a small, simple, but complete computer.

The process technology is old. The architecture is simple. But for a calculator, it is enough.

That is another important point: global electronics are not built only on cutting-edge semiconductors.

Many everyday products are still supported by old, mature, inexpensive, and reliable chips.

[Exploring Shenzhen 2026: A Field Guide to China's Hardware Capital, Urban Technology, and Real-World Innovation](https://www.amazon.com/dp/B0GHPLX7XZ)Old chips still power the worldWhen people talk about semiconductors, the conversation often goes immediately to 3nm, 2nm, AI accelerators, GPUs, and advanced packaging.

But a huge part of the world still runs on mature process nodes.

A calculator does not need an advanced processor. It needs a chip that is cheap, stable, available, and good enough.

That is why a 4-bit CPU made on an old process can still be globally relevant. It is not impressive because it is advanced. It is impressive because it is sufficient, optimized, and embedded in a massive low-cost supply chain.“Made in” is only one layerThis is not a story about saying Made in India is fake.

That would be too simple.

The real story is that modern manufacturing is layered.

A product may be assembled in India. The PCB design may come from a Chinese design house. The chip may come from a Chinese semiconductor company. The brand may belong to a trading company. The same product family may be sold under multiple names in different markets.

All of these layers can exist at the same time.

So when we see Made in India, Made in China, or Made in Japan, we should not treat it as the whole story. It is one label on top of a much deeper structure.

Teardown helps us see those layers.From a calculator to the global supply chainThis is why I like low-cost products.

Expensive products often come with a carefully designed brand story. Low-cost products are more honest. They show where cost was reduced, which components were reused, which design decisions were made, and which supply chain made the product possible.

A one-dollar calculator can connect India’s manufacturing ambitions, China’s low-cost semiconductor ecosystem, Shenzhen’s decap services, Japanese calculator history, global ODM and trading networks, and the ambiguity of “Made in” labels.

That is a lot of information hidden in a very small product.Why I talked about this at Teardown 2026At Teardown 2026, I wanted to bring a Shenzhen-based perspective to the teardown community.

[What $10 Fake AirPods and a $30 Chip Decap Reveal About China's Semiconductors | Teardown 2026 | Crowd Supply](https://www.crowdsupply.com/teardown/portland-2026/long-talk/what-10-fake-airpods-and-a-30-chip-decap-reveal-about-chinas-semiconductors)

Shenzhen is not only a place where products are assembled. It is a place where components, repair, reverse engineering, small-batch manufacturing, design services, and informal technical knowledge are all connected.

Chip decap is one example of that.

Chinese teardown media is another.

Fake AirPods are another.

Each of these examples shows that teardown is not only about curiosity. It can be a way to understand how manufacturing ecosystems actually work.A small preview of my Teardown talkIn my opening talk, I discussed several connected topics:

How chip decap services can be ordered in Shenzhen.
 How Chinese teardown media analyzes low-cost and counterfeit electronics.
 What fake AirPods reveal about China’s hardware ecosystem.
 Why old process nodes and simple chips still matter.
 How teardown can reveal the “center of gravity” of manufacturing.

The calculator story is only one entry point.

But it is a good one, because it starts from something very ordinary.

A cheap calculator.
 A black epoxy chip.
 A simple question: what is really inside?Video versionI also made a video version of this story.[https://medium.com/media/c1a2efe1e95be927c1933ab4d14b1b75/href](https://medium.com/media/c1a2efe1e95be927c1933ab4d14b1b75/href)ClosingFor me, teardown is not just about opening products.

It is a way to see how the world is connected.

A cheap calculator bought in India led to a Chinese 4-bit CPU, a Shenzhen decap service, Techanalye’s analysis, and a broader discussion at Teardown 2026.

That is why I keep doing this.

Because sometimes, the best way to understand global manufacturing is not to start with a market report.

It is to open a one-dollar calculator.

[Exploring Shenzhen 2026 - A Field Guide to China's Hardware Ecosystem](https://gumroad.com/l/jeiskh)
