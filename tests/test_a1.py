from taskforge.manager import TaskManager


def test_completed_task_not_in_pending():
    manager = TaskManager()
    task = manager.add("Buy milk")
    manager.complete(task["id"])
    assert manager.list_tasks("pending") == []


def test_completed_task_in_completed_list():
    manager = TaskManager()
    task = manager.add("Buy milk")
    manager.complete(task["id"])
    result = manager.list_tasks("completed")
    assert len(result) == 1
    assert result[0]["title"] == "Buy milk"


def test_only_the_completed_task_changes():
    manager = TaskManager()
    first = manager.add("Task one")
    manager.add("Task two")
    manager.complete(first["id"])
    pending = manager.list_tasks("pending")
    assert [t["title"] for t in pending] == ["Task two"]


def test_new_task_is_pending():
    manager = TaskManager()
    manager.add("Fresh task")
    assert len(manager.list_tasks("pending")) == 1
    assert manager.list_tasks("completed") == []


def test_list_without_status_shows_all():
    manager = TaskManager()
    first = manager.add("Task one")
    manager.add("Task two")
    manager.complete(first["id"])
    assert len(manager.list_tasks()) == 2