from taskforge.search import search_tasks

def test_exact_case_search():
    tasks = [{"id": 1, "title": "Learn Python"}]
    assert len(search_tasks(tasks, "Python")) == 1
def test_search_tasks_ignores_case():
    from taskforge.search import search_tasks

    tasks = [
        {"id": 1, "title": "Learn Python"},
        {"id": 2, "title": "LEARN PYTHON"},
        {"id": 3, "title": "learn python"},
        {"id": 4, "title": "Learn Java"},
    ]

    results = search_tasks(tasks, "python")

    assert len(results) == 3
    assert [task["id"] for task in results] == [1, 2, 3]


def test_search_does_not_modify_task_titles():
    from taskforge.search import search_tasks

    tasks = [{"id": 1, "title": "Learn PYTHON"}]

    search_tasks(tasks, "python")

    assert tasks[0]["title"] == "Learn PYTHON"
