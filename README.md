# One Word for Your Wi-Fi — "Houdini"

[![One Word for Your Wi-Fi](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Rank](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/emafajriana/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72-entry/rank.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Reward](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/emafajriana/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72-entry/reward.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)

A [make.fun](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72) entry for the "One Word for Your Wi-Fi" bounty: one word describing your Wi-Fi, judged on fit, laugh, truth and freshness.

## The entry

**Houdini** — home Wi-Fi does its best escape-artist impression: there for the video call, gone the second the call matters, back again like nothing happened. Funny at once, instantly understood with no context, true to how home Wi-Fi actually behaves, and a fresh angle on the most familiar annoyance (the signal vanishing) rather than the words everyone reaches for.

## How it works

`main.py` (Python 3.13, standard library only) writes the word to `entry.txt` in the output directory (`MAKEFUN_OUTPUT_DIR`, or `/output` by default), then reads it back and verifies it in full: UTF-8 text, 1–20 characters, a single word of letters only.

Run it:

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
