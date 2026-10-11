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
    updated = manager.complete(task["id"])
    assert updated["completed"] is True
    assert len(manager.list_tasks(status="completed")) == 1
    assert len(manager.list_tasks(status="pending")) == 0

def test_delete_unknown_task():
    with pytest.raises(ValueError, match="Task not found"):
        TaskManager().delete(999)

def test_unique_ids_after_delete():
    manager = TaskManager()
    t1 = manager.add("Task 1")
    t2 = manager.add("Task 2")
    manager.delete(t1["id"])
    t3 = manager.add("Task 3")
    assert t3["id"] == 3
    assert t3["id"] != t2["id"]

def test_add_whitespace_or_empty_title():
    manager = TaskManager()
    with pytest.raises(ValueError, match="Task title must not be empty"):
        manager.add("   ")
    with pytest.raises(ValueError, match="Task title must not be empty"):
        manager.add("")

