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

def test_complete_task():
    manager = TaskManager()
    task = manager.add("Learn Git")

    manager.complete(task["id"])

    assert task["completed"] is True
    assert task not in manager.list_tasks("pending")
    assert task in manager.list_tasks("completed")

