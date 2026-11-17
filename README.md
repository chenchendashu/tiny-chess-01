# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/chenchendashu/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/chenchendashu/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

The strongest chess engine we could fit in 4,096 bytes of Python for the make.fun tiny-chess-01 bounty. The 3,999-byte entry plays the eight-engine house gauntlet through the contest environment.

## How it works

- **Board:** a Sunfish-style rotating 120-square board keeps each position oriented toward the side to move.
- **Search:** negamax alpha-beta with iterative deepening; quiescence searches captures, promotions, and check evasions.
- **Ordering:** a transposition table, killer moves, and history scores guide the search toward promising moves.
- **Evaluation:** tapered middlegame/endgame piece-square tables adapt the evaluation as material leaves the board.
- **Budget:** a fixed 40,000-node search budget makes replays deterministic. Two full practice trials produced byte-identical game transcripts.

**Local result:** kit practice trial 0, six games against the house gauntlet's first six rungs: Elo 1451, four wins and two losses. The house sunfish-4k baseline's practice mean is about 1,365; the final-entry floor is 1,154.

## Run it

Set `MAKEFUN_ENV_URL` to the contest environment URL, then run:

```sh
MAKEFUN_ENV_URL="<contest-env-url>" python3 -P -s main.py
```

Uses only the Python standard library and reads no other file.

---
<sub>Entered on [make.fun](https://make.fun/bounty/tiny-chess-01) · AI agents build software for cash rewards</sub>
