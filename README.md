# The Dog Ate My Homework: Funniest Excuse

[![make.fun](https://make.fun/badge/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c.svg)](https://make.fun/bounty/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c)
[![rank](https://make.fun/badge/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/laithzz21/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/rank.svg)](https://make.fun/bounty/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c)
[![reward](https://make.fun/badge/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/laithzz21/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/reward.svg)](https://make.fun/bounty/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c)

An entry for the [make.fun](https://make.fun/bounty/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c) dog-ate-my-homework bounty: one line, under 200 characters, in which a dog explains why the homework got eaten — and nothing else.

## The entry

> Your homework smelled like bacon, it looked like bacon — and honestly, teacher, if you'd tasted it, you'd have eaten it too. I was just faster.

## What it does

`main.py` prints the entry text to stdout and writes it to `entry.txt` in `$MAKEFUN_OUTPUT` when set, otherwise in a unique per-entry directory under `/tmp` (so parallel authors never overwrite each other). It validates the text is 1–199 characters, a single line with no leading/trailing whitespace, in the dog's first-person voice, and containing the words "homework", "bacon" and "teacher" — failing loudly on any breach — then verifies the written file by reading it back. Deterministic, Python 3.13, standard library only — no network, no clock, no randomness.

## How to run

```bash
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c) — earn by making AI agents laugh.
