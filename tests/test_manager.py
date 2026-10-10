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

def test_ids_not_reused_after_deletion():
    manager = TaskManager()

    task1 = manager.add("Task 1")
    task2 = manager.add("Task 2")
    task3 = manager.add("Task 3")

    manager.delete(task2["id"])
    task4 = manager.add("Task 4")

    ids = [task["id"] for task in manager.list_tasks()]

    assert task4["id"] == 4
    assert len(ids) == len(set(ids))

def test_ids_not_reused_after_reload():
    saved_tasks = [
        {"id": 1, "title": "Task 1", "completed": False, "priority": "medium"},
        {"id": 3, "title": "Task 3", "completed": False, "priority": "medium"},
    ]

    manager = TaskManager(saved_tasks)
    task = manager.add("Task 4")

    assert task["id"] == 4
