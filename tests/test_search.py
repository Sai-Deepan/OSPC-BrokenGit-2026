from taskforge.search import search_tasks


def test_exact_case_search():
    tasks = [{"id": 1, "title": "Learn Python"}]
    assert len(search_tasks(tasks, "Python")) == 1


def test_search_is_case_insensitive_without_changing_titles():
    tasks = [
        {"id": 1, "title": "Learn Python"},
        {"id": 2, "title": "PYTHON Packaging"},
        {"id": 3, "title": "Learn Java"},
    ]
    original_titles = [task["title"] for task in tasks]

    assert search_tasks(tasks, "python") == tasks[:2]
    assert search_tasks(tasks, "pYtHoN") == tasks[:2]
    assert search_tasks(tasks, "yth") == tasks[:2]
    assert search_tasks(tasks, "ruby") == []
    assert [task["title"] for task in tasks] == original_titles
