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

@pytest.mark.parametrize("title", ["", "   ", "\t\n"])
def test_add_rejects_empty_or_whitespace_title(title):
    with pytest.raises(ValueError):
        TaskManager().add(title)


def test_add_accepts_valid_title():
    task = TaskManager().add("Read docs")
    assert task["title"] == "Read docs"
