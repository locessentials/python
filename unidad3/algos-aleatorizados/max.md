---
layout: default
title: Max
parent: Algoritmos aleatorizados
grandparent: 3. Matemáticas y algoritmos
nav_order: 1
---

# Max

Shows the main idea of the page: the algorithm stays the same, and the order of the input decides how much work it does.

## Hiring problem

The hiring problem is a made-up story that textbooks use to explain the idea. Here's the setup:

- You need to hire an office assistant, and an agency sends you **one candidate per day**.
- You interview each one, and if they're **better than your current assistant**, you fire the current one and hire the new person right away.
- Interviewing is cheap, but **hiring is expensive**: there's a fee each time, plus the cost of training someone new.

The question is **how many times you'll end up hiring.**

**The connection to `max`**

Your code does the same thing, just with numbers instead of people:

| Hiring story | Your code |
|---|---|
| Each candidate | Each number `i` in the list |
| Your current assistant | `max` |
| "Is this candidate better?" | `if i > max:` |
| Hiring them | `max = i` |
| Number of hires | Number of times `max` gets updated |

Counting how many times `max` changes is the same as counting how many people you hired.

**Why the order matters**

- If the candidates arrive **from worst to best** (like your ascending list), each one is better than the last, so you hire **everyone**. That's n hires, the most expensive case.
- If the **best candidate comes first**, you hire once and never again.
- If they arrive in **random order**, you hire about **ln n** times on average, which is very few. With 100 candidates it's about 5 hires.

**Where the "randomized algorithm" comes in**

You don't control the order the agency uses. It might happen to send candidates worst to best. The fix is to get the whole list from the agency in advance and **shuffle it yourself** before interviewing. Then no input order can force the worst case, and you're guaranteed the low expected cost whatever the agency does.

That's the same thing `qsr` does. A sorted list is the worst case for `qsf`, and picking the pivot at random means no particular input can force that worst case.

There's a related puzzle called the **secretary problem**, where you have to decide on the spot whether to hire someone and can't change your mind later. That one asks a different question (how to pick the single best candidate), so don't confuse the two if you come across it.

The problem asks how many times max gets updated during the scan, not what the maximum is.

With the list in ascending order, like your a, every element beats the previous maximum, so max updates n times. That's the worst case.
Shuffle the list randomly first and the expected number of updates drops to about ln n.

## Build out plan

Build it into a series of problems, each one adding a little to the last:

Count the updates. Add a counter that goes up every time max changes, and return both the maximum and the count.
Best and worst case. Run it on your sorted list a (ascending: 8 updates, the worst case) and on the same list reversed (1 update, the best case).
Shuffle it. Use random.shuffle(a) and run it again. The count will be different each time.
Average over many runs. Shuffle and count, say, 10,000 times, then take the average. For n = 8 it should come out around 2.72.
Compare with the theory. The expected number of updates is 1 + 1/2 + 1/3 + … + 1/n, called the harmonic number Hₙ, which grows like ln n. For n = 8, that's ≈ 2.718, so your average from step 4 should land close to it.