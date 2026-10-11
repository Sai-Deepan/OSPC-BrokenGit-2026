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


def test_task_id_not_reused_after_deletion():
    manager = TaskManager()
    manager.add("First")
    second = manager.add("Second")
    manager.add("Third")

    manager.delete(second["id"])
    fourth = manager.add("Fourth")

    assert fourth["id"] == 4
    assert len({task["id"] for task in manager.list_tasks()}) == 3
