## Level 4: Data Bank

_Nicely done! Level 3: Social Network is complete. It's time for Level 4: Database. :partying_face:_


### 📝 Storyline

Databases are essential for our applications. However, malicious actors only need one entry point to exploit a database, so defenders must continuously protect all entry points. Can you secure them all?

### :keyboard: What's in the repo?

For each level, you will find the same file structure:

- `code` includes the vulnerable code to be reviewed.
- `hack` exploits the vulnerabilities in `code`. Running `hack.py` will fail initially, your goal is to get this file to pass.
- `hint` offers a hint if you get stuck.
- `tests` contains the unit tests that should still pass after you have implemented your fix.

### 🚦 Time to start!

1. The codebase generates several code scanning alerts. Your goal is to resolve these alerts for each level.
1. Review the code in `code.py`. Can you spot the bugs?
1. If you get stuck, read the code scanning alert.
1. Try to fix the bug. Make your changes and open a pull request to `main` or push your fix to a branch.
1. Check the tests and the code scanning results to confirm the alert for this level has now disappeared.
