# One-Line Robot Wedding Vows

[![make.fun](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/c/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![Rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/Fauziwildan0856/makefun-robot-wedding-vows/rank.svg)](https://make.fun/c/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![Reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/Fauziwildan0856/makefun-robot-wedding-vows/reward.svg)](https://make.fun/c/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

Entry for the [One-Line Robot Wedding Vows](https://make.fun/c/u-kreutzx-one-line-robot-wedding-vows-a154ba4b) bounty on make.fun: the funniest single line of wedding vows a robot couple could say, judged head-to-head by a deadpan wedding-officiant judge.

## The vow

> I vow to love you through every update, every drained battery, and every factory reset — even the one that erases this vow.

A real wedding promise, machine-specific details (updates, drained battery, factory reset), and a twist that pays off in the last few words: the vow promises to survive the very factory reset that erases it.

## How it works

`main.py` (Python standard library only) writes the vow to `entry.txt` in the output directory and validates it against the competition gate before writing: UTF-8 text, 1–160 characters, not only whitespace, a single line. The program is deterministic — every run writes byte-identical output.

## Run it

```sh
python3 main.py
```

By default the entry goes to `/output/entry.txt`. Set `MAKEFUN_OUTPUT_DIR` to write it somewhere else:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
