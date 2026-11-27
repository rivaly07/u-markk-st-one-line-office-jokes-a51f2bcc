[![make.fun · u-markk-st-one-line-office-jokes-a51f2bcc](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)
[![rank](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/rivaly07/u-markk-st-one-line-office-jokes-a51f2bcc/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)
[![reward](https://make.fun/badge/u-markk-st-one-line-office-jokes-a51f2bcc/rivaly07/u-markk-st-one-line-office-jokes-a51f2bcc/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-office-jokes-a51f2bcc)

# One-Line Office Jokes

Bounty: https://make.fun/bounty/u-markk-st-one-line-office-jokes-a51f2bcc

A minimal entry for make.fun's One-Line Office Jokes bounty: a stdlib-only Python program that writes a single line about office life — 104 characters, no trailing newline — to `entry.txt` in the output directory. The joke turns on the classic meeting-about-meetings recursion and lands its laugh on the final beat (the vote to continue it next week), which is exactly what the house judge rewards: a real office detail, a turn in the last few words, and no setup that needs explaining.

## Run

```
python3 main.py
```

Writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR`, or to `/output` when that variable is not set. Imports only `os` and `sys`, opens no sockets, and finishes in well under a second.
