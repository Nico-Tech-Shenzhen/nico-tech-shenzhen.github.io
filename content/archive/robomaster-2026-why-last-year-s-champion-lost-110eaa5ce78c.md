---
title: "RoboMaster 2026: Why Last Year’s Champion Lost"
date: 2026-08-16T05:28:06+00:00
tags: ["robomasters"]
source: "https://medium.com/shenzhen-high-tour-by-makers/robomaster-2026-why-last-years-champion-lost-110eaa5ce78c"
---

Field notes from Shenzhen on changing rules, autonomous robots, and why RoboMaster keeps forcing even its strongest teams to rebuild.

On August 4, I was watching RoboMaster 2026 at Shenzhen Bay Sports Center when something unexpected happened quite early in the competition.

![](https://cdn-images-1.medium.com/max/1024/1*WSaUbSnSmbDbqwadvkBXCA.jpeg)

Shanghai Jiao Tong University’s Jiao Long team lost to Harbin Institute of Technology, Shenzhen.

Shanghai Jiao Tong is one of the dominant teams in RoboMaster. It won the national championship in 2021, 2023, 2024, and 2025. I already knew it had been eliminated in the quarterfinals of this year’s South China regional, but I still expected the team to be extremely strong once the national competition started.

They lost the first game against HIT Shenzhen. I remember thinking, “They might actually lose this.”

Then they lost again. In the second game, HIT Shenzhen destroyed their base and completed the win.

This was not the only upset in 2026. South China University of Technology, third nationally in 2025, also went out in the South China regional quarterfinals. South China Agricultural University, which had reached only the national top 16 last year, won the regional tournament and eventually advanced all the way to the national final.

RoboMaster has traditionally favored established teams. Universities that have participated for many years accumulate mechanical designs, software, sponsors, experienced senior students, and an enormous amount of debugging knowledge.

Watching the 2026 competition, that advantage still mattered. But it no longer looked decisive.The first obvious change: the robots look differentAfter watching several matches, one thing was immediately visible.

Many of the robots were flatter.

Parts of the field impose tighter physical constraints, so teams have developed robots that can fold their turrets or change their ride height to pass through low sections. Wheel-legged chassis are much more common as well, allowing robots to change posture and negotiate terrain that conventional four-wheel designs cannot handle as well.

The drones are smaller too. But because ground robots face tighter ammunition constraints, the drone’s ability to carry ammunition and attack from above has become relatively more important.

These are not simply design trends.

They are responses to the rules.

![](https://cdn-images-1.medium.com/max/1024/1*ubKhFdc0ijZ2Mhdw9oBirA.jpeg)

RoboMaster changes the field, robot roles, resources, and scoring system every year. In 2025, for example, two-level terrain and narrow tunnels increased the value of wheel-legged and variable-height chassis. In 2026, those ideas have developed further.

The dart system is another good example. A team may build an extremely accurate launcher one year, but if the target conditions change the following season, that system has to be reconsidered.

A highly polished version of last year’s robot is not necessarily the correct robot for this year.It is no longer mainly a game of driving and shootingRoboMaster is easy to understand at first glance: student-built robots shoot 17 mm projectiles at each other.

That is still an important part of the competition, but it no longer explains what is happening on the field.

Sentry robots move autonomously. Radar systems locate opponents. Drones attack from above. Darts target the enemy base from more than 20 meters away. Engineering robots manipulate resources on the field.

All of these roles have to work together in a 7-vs-7 match.

The competition has gradually shifted from “Who built the fastest robot with the most accurate gun?” toward a systems problem involving several different robots, sensors, human operators, and autonomous functions.

Watching Shanghai Jiao Tong lose, it was difficult to explain the result by looking at the performance of any single robot.

The whole system matters.

![](https://cdn-images-1.medium.com/max/1024/1*0G-gzYaT39TEczuruVxXYA.jpeg)

From the “vision team” to the “algorithm team”A few years ago, RoboMaster teams commonly divided their engineering work into groups for mechanics, embedded/electrical systems, and computer vision.

The vision team would use tools such as OpenCV to detect armor plates and build an auto-aim system.

Today, I increasingly hear teams use the term “algorithm team.”

The name changed because the job became much larger.

The robot has to detect an opponent, predict where it is moving, estimate its own position, navigate through the field, avoid obstacles, and in some cases decide which opponent to attack.

ROS 2, SLAM, deep learning, navigation, motion prediction, and decision-making now all appear inside the same student competition.

You can see this simply by walking around the venue. Cameras and LiDAR units are mounted all over the robots. Behind the field, teams operate several PCs running interfaces they built themselves.

Even Shanghai Jiao Tong’s 2025 infantry robot was already performing neural-network-based recognition, motion prediction, and ballistic calculation on edge computing hardware.

In 2026, those capabilities have spread much further across the competition.AI has moved into the whole robotWhat interested me most was not the appearance of some new category of “AI robot.”

![](https://cdn-images-1.medium.com/max/1024/1*SRWC8X84Kmt0rwf8luEFAQ.jpeg)

Instead, perception and autonomous algorithms have gradually entered nearly every existing part of the system.

They are used for aiming, localization, navigation, target prediction, autonomous sentries, radar, darts, and coordination between different robots.

A few years ago, an excellent auto-aim system by itself could be a major differentiator. Today, it is closer to one component inside a much larger stack.

The boundaries between mechanical design and software are also becoming harder to separate.

A low tunnel changes the chassis. A new autonomous role requires new sensors. Better localization changes the tactics. Those changes affect the operator interface and the way human players interact with the robots.

The software does not sit on top of the robot anymore. It increasingly determines what kind of robot can be built.

This is one reason I find RoboMaster increasingly interesting from the perspective of Physical AI.Why an established champion can still loseAfter watching several days of matches, Shanghai Jiao Tong’s defeat started to make more sense.

Strong teams still have enormous advantages. They have years of mechanical designs, code, experienced alumni, sponsors, test data, and accumulated knowledge.

But the problem they have to solve keeps moving.

The field changes. Robot roles change. Autonomy increases. The interaction between robots becomes more complicated.

A design that was nearly perfect last year may only be a good starting point this year.

Meanwhile, a mid-ranked team can move upward quickly if it adapts well. South China Agricultural University went from the national top 16 in 2025 to South China regional champion and national runner-up in 2026.

The national championship still went to a traditional powerhouse, Northeastern University’s TDT team. So this is not a story about established teams suddenly becoming weak.

It is a story about established teams also being forced to solve a new problem every year.RoboMaster keeps breaking last year’s solutionThe more I watched, the more important the rule changes seemed.

Add a step, and students develop wheel-legged robots.

Add a low tunnel, and they make their robots flatter.

Increase the importance of autonomous sentries, and teams work on SLAM, navigation, and decision-making.

Change the dart conditions, and even a team that achieved excellent accuracy last year has to redesign its system.

The organizers do not need to tell students, “This year, study SLAM,” or “This year, build a more autonomous robot.”

They change the problem instead.

The students respond with new technology.

When Shanghai Jiao Tong lost to HIT Shenzhen, my first reaction was simply that RoboMaster 2026 seemed unusually unpredictable.

After watching the competition for several days, I began to think the unpredictability itself was part of the design.

RoboMaster keeps making last year’s answer slightly wrong.

After more than a decade of doing this, perception, prediction, localization, navigation, and decision-making are no longer special features attached to one robot.

They are becoming part of how the entire competition works.

And even last year’s champion has to build this year’s robot.
