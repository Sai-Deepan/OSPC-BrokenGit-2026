
from taskforge.search import search_tasks


def test_exact_case_search():
    tasks = [{"id": 1, "title": "Learn Python"}]
    assert len(search_tasks(tasks, "Python")) == 1


def test_search_ignores_case():
    tasks = [{"id": 1, "title": "Learn Python"}]

    assert len(search_tasks(tasks, "python")) == 1
    assert len(search_tasks(tasks, "PYTHON")) == 1
    assert len(search_tasks(tasks, "pYtHoN")) == 1


def test_search_does_not_modify_original_title():
    tasks = [{"id": 1, "title": "Learn Python"}]

    search_tasks(tasks, "python")

    assert tasks[0]["title"] == "Learn Python"

