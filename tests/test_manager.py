import pytest
from taskforge.manager import TaskManager

def test_add_task():
    task = TaskManager().add("Read docs")
    assert task["title"] == "Read docs"
    assert task["completed"] is False

def test_complete_unknown_task():
    with pytest.raises(ValueError):
        TaskManager().complete(99)

def test_delete_task():
    manager = TaskManager()
    task = manager.add("Delete me")
    manager.delete(task["id"])
    assert manager.list_tasks() == []

def test_complete_task_updates_status():
    manager = TaskManager()
    task = manager.add("Buy groceries")
    manager.complete(task["id"])

    assert task["completed"] is True
    assert manager.list_tasks(status="pending") == []
    assert manager.list_tasks(status="completed") == [task]
