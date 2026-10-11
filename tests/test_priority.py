import pytest
from taskforge.manager import TaskManager

def test_add_task_default_priority():
    manager = TaskManager()
    task = manager.add("Default task")
    assert task["priority"] == "medium"

def test_add_task_custom_priority():
    manager = TaskManager()
    t_low = manager.add("Low task", priority="low")
    t_high = manager.add("High task", priority="high")
    assert t_low["priority"] == "low"
    assert t_high["priority"] == "high"

def test_add_task_invalid_priority():
    manager = TaskManager()
    with pytest.raises(ValueError, match="Invalid priority"):
        manager.add("Urgent task", priority="critical")

def test_filter_tasks_by_priority():
    manager = TaskManager()
    manager.add("Task 1", priority="low")
    manager.add("Task 2", priority="medium")
    manager.add("Task 3", priority="high")
    manager.add("Task 4", priority="high")

    high_tasks = manager.list_tasks(priority="high")
    assert len(high_tasks) == 2
    assert all(t["priority"] == "high" for t in high_tasks)

    low_tasks = manager.list_tasks(priority="low")
    assert len(low_tasks) == 1
    assert low_tasks[0]["title"] == "Task 1"

def test_filter_tasks_by_priority_and_status():
    manager = TaskManager()
    t1 = manager.add("High pending", priority="high")
    t2 = manager.add("High complete", priority="high")
    manager.complete(t2["id"])

    pending_high = manager.list_tasks(status="pending", priority="high")
    assert len(pending_high) == 1
    assert pending_high[0]["id"] == t1["id"]

    completed_high = manager.list_tasks(status="completed", priority="high")
    assert len(completed_high) == 1
    assert completed_high[0]["id"] == t2["id"]

def test_filter_tasks_invalid_priority():
    manager = TaskManager()
    with pytest.raises(ValueError, match="Invalid priority"):
        manager.list_tasks(priority="extreme")

def test_backward_compatibility_legacy_tasks_missing_priority():
    legacy_tasks = [
        {"id": 1, "title": "Old task 1", "completed": False},
        {"id": 2, "title": "Old task 2", "completed": True}
    ]
    manager = TaskManager(legacy_tasks)
    # Tasks without priority should default to medium
    assert manager.tasks[0]["priority"] == "medium"
    assert manager.tasks[1]["priority"] == "medium"

    medium_tasks = manager.list_tasks(priority="medium")
    assert len(medium_tasks) == 2

    high_tasks = manager.list_tasks(priority="high")
    assert len(high_tasks) == 0
