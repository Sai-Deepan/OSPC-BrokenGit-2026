import pytest

from taskforge.search import search_tasks


def test_exact_case_search():
    tasks = [{"id": 1, "title": "Learn Python"}]
    assert len(search_tasks(tasks, "Python")) == 1


def test_empty_query_returns_all_tasks():
    tasks = [
        {"id": 1, "title": "Learn Python"},
        {"id": 2, "title": "Write tests"},
    ]

    assert search_tasks(tasks, "") == tasks


def test_search_with_no_matches_returns_empty_list():
    tasks = [{"id": 1, "title": "Learn Python"}]

    assert search_tasks(tasks, "Java") == []


def test_search_rejects_non_string_query():
    with pytest.raises(ValueError, match="Search query must be text"):
        search_tasks([], 123)
