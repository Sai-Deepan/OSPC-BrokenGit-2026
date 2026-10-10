
import pytest

from taskforge.manager import TaskManager


def test_add_task():
    task = TaskManager().add("Read docs")

    assert task["title"] == "Read docs"
    assert task["completed"] is False
    assert task["priority"] == "medium"


def test_complete_unknown_task():
    with pytest.raises(ValueError):
        TaskManager().complete(99)


def test_delete_task():
    manager = TaskManager()
    task = manager.add("Delete me")

    manager.delete(task["id"])

    assert manager.list_tasks() == []


def test_add_task_with_priority():
    task = TaskManager().add("Urgent task", "high")

    assert task["priority"] == "high"


def test_add_task_defaults_to_medium_priority():
    task = TaskManager().add("Regular task")

    assert task["priority"] == "medium"


def test_unsupported_priority_is_rejected():
    with pytest.raises(ValueError, match="Priority must be one of"):
        TaskManager().add("Invalid task", "urgent")


def test_legacy_task_without_priority_defaults_to_medium():
    legacy_task = {
        "id": 1,
        "title": "Old task",
        "completed": False,
    }

    manager = TaskManager([legacy_task])

    assert manager.list_tasks()[0]["priority"] == "medium"
    assert "priority" not in legacy_task


def test_list_tasks_filters_by_priority():
    manager = TaskManager()
    manager.add("Small task", "low")
    manager.add("Normal task", "medium")
    manager.add("Urgent task", "high")

    result = manager.list_tasks(priority="high")

    assert [task["title"] for task in result] == ["Urgent task"]


def test_status_and_priority_filters_work_together():
    manager = TaskManager([
        {
            "id": 1,
            "title": "Pending high",
            "completed": False,
            "priority": "high",
        },
        {
            "id": 2,
            "title": "Completed high",
            "completed": True,
            "priority": "high",
        },
        {
            "id": 3,
            "title": "Completed low",
            "completed": True,
            "priority": "low",
        },
    ])

    result = manager.list_tasks(
        status="completed",
        priority="high",
    )

    assert [task["title"] for task in result] == ["Completed high"]


def test_unsupported_filter_priority_is_rejected():
    manager = TaskManager()

    with pytest.raises(ValueError, match="Priority must be one of"):
        manager.list_tasks(priority="urgent")
