Issue #2: Case-Insensitive Task Search

1. Overview

This document describes the fix implemented for Issue #2, [A2] Bug: search ignores case variants, in the OSPC BrokenGit repository.

2. Problem Identified

The task search function was case-sensitive. As a result, searches could fail when the capitalization of the query differed from the task title.

For example, searching for `python` would not match a task titled `Learn Python`.
3. Implementation

The function in `taskforge/search.py` was updated to convert both the search query and task titles to lowercase before comparing them.

```python
def search_tasks(tasks, query):
    if not isinstance(query, str):
        raise ValueError("Search query must be text")
    return [
        task for task in tasks
        if query.lower() in task["title"].lower()
    ]
```

This allows searches to match regardless of capitalization while preserving the original task titles. The function also validates that the query is a string.

4. Testing

Tests were added in `tests/test_search.py` for exact-case, lowercase, and mixed-case searches.

The full test suite was run using `python3 -m pytest`, and all 12 tests passed.

5. Outcome

Task searches can now find matching titles regardless of capitalization, resolving the issue.

6. Files Changed

- `taskforge/search.py` — updated the search comparison.
- `tests/test_search.py` — added tests for case-insensitive matching.

7. AI Assistance

ChatGPT was used for guidance while investigating the issue, implementing and documentation. The changes and test results were reviewed locally.