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

def test_add_rejects_empty_title():
    import pytest
    from taskforge.manager import TaskManager

    with pytest.raises(ValueError, match="Task title must not be empty"):
        TaskManager().add("")


def test_delete_nonexistent_task_raises_error():
    import pytest
    from taskforge.manager import TaskManager

    with pytest.raises(ValueError, match="Task not found"):
        TaskManager().delete(999)


def test_list_tasks_pending_filter():
    from taskforge.manager import TaskManager

    manager = TaskManager([
        {
            "id": 1,
            "title": "Pending task",
            "completed": False,
        },
        {
            "id": 2,
            "title": "Completed task",
            "completed": True,
        },
    ])

    result = manager.list_tasks(status="pending")

    assert [task["title"] for task in result] == ["Pending task"]
