from taskforge.search import search_tasks


def test_exact_case_search():
    tasks = [{"id": 1, "title": "Learn Python"}]
    assert len(search_tasks(tasks, "Python")) == 1


def test_case_insensitive_search():
    tasks = [{"id": 1, "title": "Learn Git"}]

    assert len(search_tasks(tasks, "git")) == 1
    assert len(search_tasks(tasks, "Git")) == 1
    assert len(search_tasks(tasks, "GIT")) == 1

