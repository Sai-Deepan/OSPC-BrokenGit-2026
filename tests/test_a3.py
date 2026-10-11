import pytest
from taskforge.manager import TaskManager


def test_blank_titles_rejected():
    manager = TaskManager()
    for bad in ["", "   ", "\t", "\n", " \t\n "]:
        with pytest.raises(ValueError):
            manager.add(bad)


def test_rejected_title_not_saved():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add("   ")
    assert manager.list_tasks() == []


def test_valid_title_still_works():
    task = TaskManager().add("Read docs")
    assert task["title"] == "Read docs"