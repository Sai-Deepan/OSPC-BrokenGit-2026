# OSPC Recruitment — Round 1 Submission

**Name:**  Rohit Y
**Registration Number:**  26BCE1255
**Year:**  1st year
**GitHub Username:**  rohityadav-RY
**Issue Number:** [A1] Bug: completed tasks still appear pending
good first issue


## Problem Identified
The complete() method in taskforge-->manager.py updated the dictionary key "done" instead of "completed". This changes the dictionary to add a new key value pair instead of chaning the task status from 
completed --> False to completed --> True .

## Changes Made
In the completed() method in taskforge --> manager.py , changed line no 16:
old:
                task["done"] = True  # Intentional recruitment bug A1
new:
                task["completed"] = True  # Intentional recruitment bug A1

## Testing
Ran the test suite using python -m pytest.
Result: All 6 tests passed.


## Challenges Faced
Geting to understand what the main aim of the program , also the part where the change of task happen was a bit tough.

## AI Tool Usage
yes , used chatgpt for knowing syntax and what the code actually does , but did not make it do my job. I mannualy verified what it said with the proof from the above screen shot.

## Checklist
- [ yes] I worked on my own fork and branch.
- [ yes] My changes address the selected issue.
- [ yes] I tested my changes.
- [ yes] I documented the changes.
- [ yes] I can explain my implementation during the interview.
