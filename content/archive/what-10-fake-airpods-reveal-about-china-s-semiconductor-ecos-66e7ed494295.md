---
title: "What $10 Fake AirPods Reveal About China’s Semiconductor Ecosystem"
date: 2026-06-19T12:41:58+00:00
tags: ["teardown", "semiconductors", "supply-chain", "shenzhen"]
source: "https://medium.com/shenzhen-high-tour-by-makers/what-10-fake-airpods-reveal-about-chinas-semiconductor-ecosystem-66e7ed494295"
---

A field note from Shenzhen: low-cost TWS earbuds, chip decap services, and the supply chains behind “fake” hardwareI bought a pair of “Huaqiangbei AirPods” on Taobao for 67 RMB — about 10 USD at the time.

![](https://cdn-images-1.medium.com/max/1024/1*8KIJ3FyahjHrllkj-QhyaA.jpeg)

They are clearly not genuine Apple AirPods. The packaging, the pairing screen, and the overall experience are designed to look familiar, but the product itself is a completely different piece of hardware.

That is exactly why I wanted to open them.

When we talk about counterfeit electronics, the discussion usually stops at legal or ethical issues. Those issues matter. I am not writing this to praise counterfeit products.

But as a hardware field note, a $10 pair of fake AirPods is extremely interesting.

Inside, I found a compact snapshot of China’s low-cost TWS earbud ecosystem: integrated Bluetooth audio SoCs, simplified sensors, shared left/right PCB design, erased chip markings, Taobao-based chip decap services, and Chinese teardown communities analyzing these products in detail.

This article is based on a recent episode of Nico-Tech Shenzhen Field Notes and is also a preview of my upcoming Teardown 2026 opening talk:

“What $10 Fake AirPods and a $30 Chip Decap Reveal About China’s Semiconductors.”

Teardown 2026 talk page:
[https://www.crowdsupply.com/teardown/portland-2026/long-talk/what-10-fake-airpods-and-a-30-chip-decap-reveal-about-chinas-semiconductors](https://www.crowdsupply.com/teardown/portland-2026/long-talk/what-10-fake-airpods-and-a-30-chip-decap-reveal-about-chinas-semiconductors)

For readers who want a broader guide to Shenzhen’s hardware ecosystem, I also recently released Shenzhen Field Guide 2026:
[https://takasumasakazu.gumroad.com/l/2026sz](https://takasumasakazu.gumroad.com/l/2026sz)The outside is copied. The inside is not.Genuine AirPods are highly sophisticated devices.

A modern AirPods earbud contains many chips and sensors: microphones, motion sensors, wireless audio processors, battery management, power control, and signal processing hardware for features such as noise cancellation, conversation awareness, and spatial audio.

The fake AirPods I opened were completely different.

![](https://cdn-images-1.medium.com/max/1024/1*3HdWZLVQ8NiCzluLz1CJFg.png)

Inside each earbud, I found only a small number of ICs: a main Bluetooth audio SoC, a touch sensor, a MEMS microphone, and supporting components such as a clock source.

In other words, this product does not copy Apple’s internal architecture.

Instead, it creates an “AirPods-like” experience with a much smaller and cheaper architecture.

It can pair with an iPhone or iPad. It can show a familiar-looking battery display. It can provide basic media controls. Some models even show options that resemble spatial audio, although the actual functions are only rough imitations.

The visible experience is copied.

The internal engineering is not.

That difference is important.

A fake AirPods unit is not simply a low-quality version of Apple’s product. It is a separate low-cost design optimized for a completely different price point, manufacturing process, and supply chain.Four ICs instead of a complex Apple architectureThe genuine AirPods design is dense, asymmetric, and highly optimized.

The fake one is designed around simplicity.

The version I opened used only a few major ICs. The most important one was the main Bluetooth audio SoC, likely from Jieli, one of China’s major low-cost Bluetooth audio chip vendors.

There was also a touch control IC, a MEMS microphone, and a few supporting components.

This small set of parts is enough to build a basic TWS earbud.

It will not deliver genuine AirPods-level quality. It will not provide real Apple-grade noise cancellation or spatial audio. But it is enough to create something that behaves like a wireless earbud and looks convincing to casual users.

This is one of the key lessons from low-cost hardware.

The goal is not always to reproduce the best product.

Sometimes the goal is to reproduce just enough of the user experience at one-thirtieth or one-fiftieth of the price.Shared PCB design and DFMOne of the most interesting parts of the teardown was the PCB design.

The fake AirPods used a simplified design where the left and right earbuds shared many common parts and layout decisions.

This matters because left/right differences can create manufacturing complexity. If the left and right earbuds require different PCBs, different parts, different assembly steps, or different inventory management, the cost goes up.

By using common parts and simplifying the design, the manufacturer can reduce the bill of materials, simplify procurement, buy more of the same components, and reduce assembly complexity.

This is DFM — Design for Manufacturing.

It is not Apple-style high-end engineering.

But it is still engineering.

And it is exactly the kind of engineering that makes Shenzhen interesting: not only how to build the highest-performance device, but how to build a device that is good enough for a very specific market and price.The SoC: Jieli, Bluetrum, and the low-cost TWS marketThe main chip had its marking erased.

At first, I could not identify the exact part number. But the logo, package, and pin configuration suggested that it was likely a Jieli Bluetooth audio SoC.

![](https://cdn-images-1.medium.com/max/1024/1*ZRX6GNthvJCpIylgmHOWwA.jpeg)

Jieli and Bluetrum are two of the important chip vendors in the low-cost TWS earbud market. Their chips are widely used in inexpensive Bluetooth earbuds, including many products sold in discount shops.

These chips integrate many functions into a single package: Bluetooth audio, microphone input, battery control, button or touch input, and enough GPIO to support the basic functions of a TWS earbud.

That level of integration is what makes a $10 wireless earbud possible.

In other fake AirPods models, I also found different PCBs and different SoC families, including Bluetrum-based designs.

This means there is no single “fake AirPods” design.

There are many tiers, many boards, many SoCs, and many supply-chain paths.

Some models are extremely cheap. Some are more expensive. Some look like AirPods. Some identify themselves as AirPods Pro. Some offer UI behaviors that look more advanced than the actual hardware behind them.

The “fake AirPods” market is not one product.

It is an ecosystem.Why erase the chip marking?The erased chip marking was one of the most intriguing parts of the teardown.

There are several possible reasons.

One possibility is that the product maker does not want competitors to know which SoC is being used.

![](https://cdn-images-1.medium.com/max/1024/1*-5oYI2gSXl-8W_2TiUAgcw.jpeg)

Another possibility is that the chips came from surplus inventory, second-grade distribution, failed projects, or gray-market component channels.

In Shenzhen, components can move through many different paths.

A project may fail. A company may shut down. A large batch of chips may become excess inventory. A supplier may need to convert parts into cash. Chips originally purchased for one project may quietly move into another.

If the original part number remains visible, the source, grade, or intended customer may be traceable.

Erasing the marking makes the supply chain harder to read.

I cannot prove exactly what happened in this case. But the absence of the marking itself is a clue.

In low-cost hardware ecosystems, the official supply chain and the real supply chain are not always the same thing.Chip decap services on TaobaoTo learn more, I tried chip decapsulation.

On Taobao, I found several service providers offering chip decap, polishing, bonding wire repair, chip photography, and related analysis services.

These are not large public research labs. They are small service businesses.

I sent a photo of the PCB assembly and asked whether they could decap the chip.

Within minutes, I received a quote.

The price was around 300 RMB, about 6,000 yen. If they could not produce a usable photo, they said they would refund the money. It was almost a success-based chip analysis service.

A few days later, they sent the first die photo.

The bonding wires were visible, but the number of bond pads looked too small for a multifunctional TWS SoC. My guess was that we were only seeing the upper die — likely flash memory — inside a system-in-package structure.

So I asked them to grind deeper.

After some negotiation, they agreed and sent new photos without extra charge.

The second result was much better: a cleanly polished SoC die with many bonding pads and visible layout features.

![](https://cdn-images-1.medium.com/max/1024/1*qdUO5SdiBQg2aZTWkAo8sA.jpeg)

That image matched much more closely with known teardown reports of similar Jieli chips.

For me, this was one of the most fascinating parts of the story.

In China, not only the products but also the analysis services are part of the ecosystem.

You can buy a cheap product, open it, find a mysterious chip, send it to a Taobao decap service, receive die photos, and compare them with teardown reports from Chinese communities.

This is hardware research as fieldwork.China’s semiconductor ecosystem is not only about advanced nodesWhen people talk about China’s semiconductor industry, the discussion often focuses on advanced process nodes, lithography, export controls, national policy, and geopolitical competition.

Those topics are important.

But they are not the whole story.

There is another semiconductor ecosystem at the bottom of the market: low-cost Bluetooth audio chips, microcontrollers, calculator chips, LED drivers, USB controllers, power management chips, and countless small application-specific ICs used in everyday consumer products.

These chips may not be made on the most advanced processes.

They may not appear in national strategy headlines.

But they are everywhere.

They enable discount-store gadgets, cheap wireless earbuds, electronic toys, calculators, small appliances, and the long tail of global consumer electronics.

A $10 fake AirPods teardown shows how product design, chip vendors, gray-market components, manufacturing optimization, decap services, and teardown communities are connected.

That connection is the real story.From fake AirPods to Teardown 2026Earlier this year, I also opened and decapped a very cheap calculator labeled “Made in India.”

That project led to a lot of discussion, especially on LinkedIn, because many of the parts and design patterns pointed back to China’s supply chain.

The fake AirPods teardown and the Indian calculator decap eventually became the basis for my Teardown 2026 proposal.

The talk was accepted as an opening talk.

Title:

What $10 Fake AirPods and a $30 Chip Decap Reveal About China’s Semiconductors

Teardown 2026 official page:
[https://www.crowdsupply.com/teardown/portland-2026](https://www.crowdsupply.com/teardown/portland-2026)

My talk page:
[https://www.crowdsupply.com/teardown/portland-2026/long-talk/what-10-fake-airpods-and-a-30-chip-decap-reveal-about-chinas-semiconductors](https://www.crowdsupply.com/teardown/portland-2026/long-talk/what-10-fake-airpods-and-a-30-chip-decap-reveal-about-chinas-semiconductors)

Teardown 2026 schedule:
[https://www.crowdsupply.com/teardown/portland-2026/schedule](https://www.crowdsupply.com/teardown/portland-2026/schedule)

I am especially interested in feedback from people who work on hardware, semiconductors, supply chains, reverse engineering, open hardware, or manufacturing.

The final talk will be in English, and I am using this article and the related YouTube episode as a public preview before the event.Watch the videoThis article is based on an episode of Nico-Tech Shenzhen Field Notes.

YouTube episode:[https://medium.com/media/5ae33cdebda75e7cf065eb02a57f8dcb/href](https://medium.com/media/5ae33cdebda75e7cf065eb02a57f8dcb/href)YouTube playlist:[https://medium.com/media/a0fdeec6066699d1a5629e53253a2bf9/href](https://medium.com/media/a0fdeec6066699d1a5629e53253a2bf9/href)If you are interested in Shenzhen’s hardware ecosystem, I also wrote Shenzhen Field Guide 2026:

Gumroad:
[https://takasumasakazu.gumroad.com/l/2026sz](https://takasumasakazu.gumroad.com/l/2026sz)Final thoughtA $10 fake AirPods unit is not just a counterfeit product.

It is also a small window into a much larger hardware ecosystem.

If we only look at official product launches, high-end chips, or national semiconductor policy, we miss a huge part of how electronics are actually made, copied, modified, analyzed, and distributed.

Sometimes the best way to understand an ecosystem is simple:

Buy the cheap thing.
Open it.
Look at the PCB.
Find the chip.
Grind it down.
Ask what kind of world made this possible.

That is what I want to talk about at Teardown 2026.

And that is why I keep taking apart cheap things from Shenzhen.
