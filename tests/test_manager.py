import pytest
from taskforge.manager import TaskManager
from taskforge.storage import load_tasks, save_tasks

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

def test_add_after_deletion_uses_next_id():
    manager = TaskManager()

    first = manager.add("Task one")
    second = manager.add("Task two")
    third = manager.add("Task three")

    manager.delete(second["id"])
    fourth = manager.add("Task four")

    assert fourth["id"] == 4
    assert len({task["id"] for task in manager.tasks}) == 3
    assert first["id"] < third["id"] < fourth["id"]

def test_add_after_manager_reload_uses_next_id():
    manager = TaskManager()
    manager.add("Task one")
    manager.add("Task two")
    manager.add("Task three")
    manager.delete(2)

    # Simulate reconstructing a manager from stored task records.
    reloaded_manager = TaskManager(manager.tasks)
    new_task = reloaded_manager.add("Task four")

    assert new_task["id"] == 4
    assert len({
        task["id"] for task in reloaded_manager.tasks
    }) == 3

def test_add_after_deleting_highest_id():
    manager = TaskManager()

    manager.add("Task one")
    manager.add("Task two")
    third = manager.add("Task three")

    manager.delete(third["id"])
    new_task = manager.add("Task four")

    assert new_task["id"] == 4
def test_ids_after_deletion_and_disk_reload(tmp_path):
    storage_path = tmp_path / "tasks.json"
    manager = TaskManager()

    manager.add("Task one")
    manager.add("Task two")
    manager.add("Task three")

    manager.delete(2)
    save_tasks(manager.tasks, storage_path)

    # Simulate a fresh CLI session loading tasks from disk.
    reloaded_manager = TaskManager(load_tasks(storage_path))
    new_task = reloaded_manager.add("Task four")

    assert new_task["id"] == 4
    assert [task["id"] for task in reloaded_manager.tasks] == [1, 3, 4]
