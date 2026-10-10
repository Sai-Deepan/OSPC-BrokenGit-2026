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

    task1 = manager.add("Task A")
    task2 = manager.add("Task B")
    task3 = manager.add("Task C")

    manager.delete(task2["id"])

    task4 = manager.add("Task D")

    assert task1["id"] == 1
    assert task3["id"] == 3
    assert task4["id"] == 4
def test_ids_not_reused_after_deleting_highest_id():
    manager = TaskManager()

    manager.add("Task A")
    task2 = manager.add("Task B")
    manager.add("Task C")

    manager.delete(task2["id"])

    task4 = manager.add("Task D")

    assert task4["id"] == 4
