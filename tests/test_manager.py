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

    first = manager.add("First")
    second = manager.add("Second")
    third = manager.add("Third")

    manager.delete(second["id"])
    fourth = manager.add("Fourth")

    assert [first["id"], third["id"], fourth["id"]] == [1, 3, 4]
    assert len({task["id"] for task in manager.list_tasks()}) == 3


def test_ids_continue_after_reload():
    previously_stored_tasks = [
        {"id": 1, "title": "First", "completed": False, "priority": "medium"},
        {"id": 3, "title": "Third", "completed": False, "priority": "medium"},
    ]

    reloaded_manager = TaskManager(tasks=previously_stored_tasks)
    new_task = reloaded_manager.add("Fourth")

    assert new_task["id"] == 4
