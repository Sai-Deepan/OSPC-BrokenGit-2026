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

def test_id_not_reused_after_deletion():
    manager = TaskManager()
    manager.add("Task 1")
    manager.add("Task 2")
    manager.add("Task 3")
    
    manager.delete(2)
    task4 = manager.add("Task 4")
    
    assert task4["id"] == 4
