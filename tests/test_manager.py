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

def test_completed_task_not_in_pending():
    manager = TaskManager()
    task = manager.add("Write report")
    manager.complete(task["id"])

    pending = manager.list_tasks(status="pending")
    assert task["id"] not in [t["id"] for t in pending]


def test_completed_task_in_completed():
    manager = TaskManager()
    task = manager.add("Write report")
    manager.complete(task["id"])

    completed = manager.list_tasks(status="completed")
    assert task["id"] in [t["id"] for t in completed]


def test_other_tasks_stay_pending():
    manager = TaskManager()
    first = manager.add("Task one")
    second = manager.add("Task two")
    manager.complete(first["id"])

    pending_ids = [t["id"] for t in manager.list_tasks(status="pending")]
    assert pending_ids == [second["id"]]
