import pytest
from taskforge.search import search_tasks

def test_exact_case_search():
    tasks = [{"id": 1, "title": "Learn Python"}]
    assert len(search_tasks(tasks, "Python")) == 1

def test_case_insensitive_search():
    tasks = [{"id": 1, "title": "Learn Git"}, {"id": 2, "title": "Write Code"}]
    results = search_tasks(tasks, "git")
    assert len(results) == 1
    assert results[0]["id"] == 1

def test_search_invalid_query_type():
    with pytest.raises(ValueError, match="Search query must be text"):
        search_tasks([], 123)

def test_search_empty_query():
    tasks = [{"id": 1, "title": "Task A"}, {"id": 2, "title": "Task B"}]
    assert len(search_tasks(tasks, "")) == 2

def test_search_no_matching_results():
    tasks = [{"id": 1, "title": "Task A"}]
    assert search_tasks(tasks, "nonexistent") == []

def test_search_substring():
    tasks = [{"id": 1, "title": "Refactor codebase"}]
    assert len(search_tasks(tasks, "code")) == 1


