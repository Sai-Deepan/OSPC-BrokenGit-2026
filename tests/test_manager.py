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


def test_ids_are_not_reused_after_deletion():
    manager = TaskManager()
    manager.add("First task")
    second = manager.add("Second task")
    manager.add("Third task")

    manager.delete(second["id"])
    fourth = manager.add("Fourth task")

    assert fourth["id"] == 4
    assert len({task["id"] for task in manager.tasks}) == 3


def test_ids_remain_unique_after_manager_reload():
    manager = TaskManager()
    manager.add("First task")
    second = manager.add("Second task")
    manager.add("Third task")

    manager.delete(second["id"])

    reloaded_manager = TaskManager(manager.tasks)
    new_task = reloaded_manager.add("Fourth task")

    assert new_task["id"] == 4
    assert len({task["id"] for task in reloaded_manager.tasks}) == 3
