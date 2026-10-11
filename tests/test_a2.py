from taskforge.manager import TaskManager
from taskforge.search import search_tasks


def test_search_ignores_case():
    manager = TaskManager()
    manager.add("Learn Git")
    for query in ["git", "GIT", "Git", "learn git"]:
        assert len(search_tasks(manager.tasks, query)) == 1


def test_search_no_match():
    manager = TaskManager()
    manager.add("Learn Git")
    assert search_tasks(manager.tasks, "python") == []


def test_search_returns_only_matching_tasks():
    manager = TaskManager()
    manager.add("Learn Git")
    manager.add("Buy milk")
    result = search_tasks(manager.tasks, "MILK")
    assert [t["title"] for t in result] == ["Buy milk"]