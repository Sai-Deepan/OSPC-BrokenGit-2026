import pytest
from taskforge.manager import TaskManager
from taskforge.validator import validate_title

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


def test_whitespace_only_title_rejection():
    with pytest.raises(ValueError):
        validate_title("   ")
    with pytest.raises(ValueError):
        validate_title("\t")
