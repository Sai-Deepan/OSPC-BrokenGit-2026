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

def test_completed_task_moves_from_pending_to_completed():
    manager = TaskManager()
    done = manager.add("Finish me")
    still_pending = manager.add("Leave me")
    manager.complete(done["id"])
    assert done["completed"] is True
    assert manager.list_tasks("pending") == [still_pending]
    assert manager.list_tasks("completed") == [done]
