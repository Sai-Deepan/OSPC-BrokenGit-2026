# Operation: Broken Source — OSPC Open Source Recruitment 2026

**Duration:** 24 hours from the organizer-announced start time.  
**Tracks:** Freshers (A) and Seniors (B).  
**Mission:** Fork, investigate, fix ONE issue, test, and submit ONE pull request.

## Quick start

Requires Python 3.10+.

```bash
python -m pip install -r requirements.txt
python -m pytest
python main.py add "Learn Git"
python main.py list
```

**Known limitation:** The starter project contains deliberate bugs and incomplete features. Some commands will not work correctly until their associated issue is solved. A green baseline test suite does NOT mean the application is bug-free.

## CLI commands

```bash
python main.py add "Learn Git"
python main.py list
python main.py list --status pending
python main.py complete 1
python main.py delete 1
python main.py search git
```

## Task storage

Tasks are saved as UTF-8 JSON in `tasks.json` in the current working directory.
Run commands from the same directory to keep using the same task list. A
missing file starts an empty list; successful commands save the current tasks,
including an empty list after deleting the last task.

If the file contains malformed JSON or does not contain a JSON list, the CLI
reports an error without overwriting it. Fix the file, or back it up and move it
aside before running another command to start with an empty task list.

## Choosing your issue

Read the GitHub Issues tab after the organizers publish the issue descriptions. Choose **one** issue in your track. The issue descriptions are also available in the organizer handoff package (not this public repository). Multiple candidates may work on the same issue.

## Submission

1. Fork the repo.
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/OSPC-BrokenSource-2026.git`.
3. Create a branch: `git switch -c fix/issue-id-description`.
4. Make changes and run `python -m pytest`.
5. Commit and push: `git add . && git commit -m "fix: describe issue" && git push -u origin fix/issue-id-description`.
6. Open a PR to the organizer repository's `main` branch; fill in the PR template.
7. Submit the PR URL using the organizer's form before the deadline. **Do not merge your own PR.**

See [CONTRIBUTING.md](CONTRIBUTING.md) for the rules. AI assistance is permitted with disclosure; you must be able to explain your work.
