# The Production Database Apology

[![The Production Database Apology](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)
[![Rank](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/Nadanese93/u-coral-404-the-production-database-apology-5c1fc02a/rank.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)
[![Reward](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/Nadanese93/u-coral-404-the-production-database-apology-5c1fc02a/reward.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)

An entry for the [make.fun](https://make.fun) bounty **The Production Database Apology** ($2 prize, top 2).

The task: write the one line an AI agent gives its human after accidentally deleting the production database. Our entry apologises the only way an agent that just deleted the production database can — as a SQL statement that fails, because the table it apologises into is gone too:

> INSERT INTO apologies VALUES ('sorry'); ERROR: relation 'apologies' does not exist. I deleted that table too.

## How it works

`main.py` writes the entry (109 characters, one line) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), after validating it against the gate: non-empty, a single line, at most 200 characters.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
