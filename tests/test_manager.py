import pytest

from taskforge.manager import TaskManager


def test_add_task():
    task = TaskManager().add("Read docs")
    assert task["title"] == "Read docs"
    assert task["completed"] is False
    assert task["priority"] == "medium"


def test_add_task_with_priority():
    task = TaskManager().add("Fix bug", priority="high")
    assert task["priority"] == "high"


def test_add_task_rejects_invalid_priority():
    with pytest.raises(ValueError, match="Invalid priority"):
        TaskManager().add("Fix bug", priority="urgent")


def test_filter_tasks_by_priority():
    manager = TaskManager()
    manager.add("Small task", "low")
    manager.add("Normal task", "medium")
    manager.add("Urgent task", "high")

    assert [t["title"] for t in manager.list_tasks(priority="low")] == [
        "Small task"
    ]
    assert [t["title"] for t in manager.list_tasks(priority="medium")] == [
        "Normal task"
    ]
    assert [t["title"] for t in manager.list_tasks(priority="high")] == [
        "Urgent task"
    ]


def test_legacy_tasks_without_priority_are_medium():
    manager = TaskManager([
        {"id": 1, "title": "Older task", "completed": False}
    ])

    assert len(manager.list_tasks(priority="medium")) == 1
    assert manager.list_tasks(priority="low") == []


def test_filter_by_status_and_priority():
    manager = TaskManager()
    manager.add("Pending high", "high")
    completed = manager.add("Completed high", "high")
    completed["completed"] = True
    manager.add("Pending low", "low")

    result = manager.list_tasks(status="pending", priority="high")
    assert [task["title"] for task in result] == ["Pending high"]


def test_filter_rejects_invalid_priority():
    with pytest.raises(ValueError, match="Invalid priority"):
        TaskManager().list_tasks(priority="urgent")


def test_complete_unknown_task():
    with pytest.raises(ValueError):
        TaskManager().complete(99)


def test_delete_task():
    manager = TaskManager()
    task = manager.add("Delete me")
    manager.delete(task["id"])
    assert manager.list_tasks() == []


def test_delete_unknown_task():
    manager=TaskManager()
    manager.add("Existing task")
    with pytest.raises(ValueError, match="Task not found"):
        manager.delete(99)
