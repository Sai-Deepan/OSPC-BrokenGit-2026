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

def test_reject_whitespace_only_title():
    """Whitespace-only titles should be rejected with ValueError."""
    with pytest.raises(ValueError):
        TaskManager().add("   ")

def test_reject_empty_title():
    """Empty titles should be rejected with ValueError."""
    with pytest.raises(ValueError):
        TaskManager().add("")

def test_reject_tab_only_title():
    """Tab-only titles should be rejected with ValueError."""
    with pytest.raises(ValueError):
        TaskManager().add("\t")
