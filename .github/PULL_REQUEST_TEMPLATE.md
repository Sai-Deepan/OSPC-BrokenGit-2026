# OSPC Recruitment — Round 1 Submission

**Sayan Sanai:**  
**26BCE5406:**  
**1st year:**  
**sayzz-06:**  
**Issue Number:**

## Problem Identified
In main.py  manager = TaskManager(load_tasks()) is written outside the try block

## Changes Made
The manager = TaskManager(load_tasks()) is written inside the task block.
try block ensures that any file-loading errors or parsing issues are  caught and handled by   parser.exit(1, f"Error: {exc}\n") in except block

## Testing
Describe tests performed, results, and commands or screenshots if useful.

## Challenges Faced
I have done this thing for the first time as I am a fresher. I couldn't understand most of the things. But while visiting the main.py file I thougt this could be a major bug.

## AI Tool Usage
I used gemini to know how to access the github file.

## Checklist
- [ok] I worked on my own fork and branch.
- [ok] My changes address the selected issue.
- [ ] I tested my changes.
- [ok] I documented the changes.
- [ok] I can explain my implementation during the interview.
