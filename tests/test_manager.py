import pytest
from taskforge.manager import TaskManager
from taskforge.storage import save_tasks, load_tasks

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


def test_deleted_task_id_is_not_reused():
    manager = TaskManager()

    first = manager.add("Task one")
    second = manager.add("Task two")
    third = manager.add("Task three")

    manager.delete(second["id"])
    fourth = manager.add("Task four")

    ids = [task["id"] for task in manager.list_tasks()]

    assert fourth["id"] not in {
        first["id"],
        third["id"],
    }
    assert len(ids) == len(set(ids))
    assert fourth["id"] > third["id"]


def test_next_id_uses_highest_existing_id():
    existing_tasks = [
        {"id": 1, "title": "Task one", "completed": False, "priority": "medium"},
        {"id": 3, "title": "Task three", "completed": False, "priority": "medium"},
    ]

    manager = TaskManager(existing_tasks)
    new_task = manager.add("Task four")

    assert new_task["id"] == 4
    assert len({task["id"] for task in manager.list_tasks()}) == 3



def test_task_ids_remain_unique_after_reload(tmp_path):
    path = tmp_path / "tasks.json"
    manager = TaskManager()

    manager.add("Task one")
    second = manager.add("Task two")
    manager.add("Task three")

    manager.delete(second["id"])
    save_tasks(manager.list_tasks(), path)

    reloaded_manager = TaskManager(load_tasks(path))
    new_task = reloaded_manager.add("Task four")

    ids = [task["id"] for task in reloaded_manager.list_tasks()]

    assert new_task["id"] == 4
    assert len(ids) == len(set(ids))
