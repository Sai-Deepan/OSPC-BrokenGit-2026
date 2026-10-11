import pytest
from taskforge.manager import TaskManager

def test_add_task_default_priority():
    manager = TaskManager()
    task = manager.add("Test task")
    assert task["priority"] == "medium"

def test_add_task_custom_priority():
    manager = TaskManager()
    task = manager.add("High priority task", priority="high")
    assert task["priority"] == "high"

def test_add_task_invalid_priority():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add("Bad task", priority="urgent")

def test_list_tasks_by_priority():
    manager = TaskManager()
    manager.add("Task 1", priority="low")
    manager.add("Task 2", priority="high")
    manager.add("Task 3", priority="low")

    low_tasks = manager.list_tasks(priority="low")
    assert len(low_tasks) == 2
    assert all(t["priority"] == "low" for t in low_tasks)

def test_backward_compatibility_missing_priority():
    old_task = {"id": 1, "title": "Old task without priority", "completed": False}
    manager = TaskManager([old_task])
    
    medium_tasks = manager.list_tasks(priority="medium")
    assert len(medium_tasks) == 1
    assert medium_tasks[0]["title"] == "Old task without priority"
