
import pytest

from taskforge.search import search_tasks


def test_exact_case_search():
    tasks = [{"id": 1, "title": "Learn Python"}]

    assert len(search_tasks(tasks, "Python")) == 1


def test_search_returns_empty_list_when_no_match():
    tasks = [{"id": 1, "title": "Learn Python"}]

    assert search_tasks(tasks, "Java") == []


def test_search_rejects_non_string_query():
    tasks = [{"id": 1, "title": "Learn Python"}]

    with pytest.raises(ValueError, match="Search query must be text"):
        search_tasks(tasks, 123)
