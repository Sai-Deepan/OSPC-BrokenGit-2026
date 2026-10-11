from taskforge.manager import TaskManager


def test_completed_task_moves_from_pending_to_completed():
    manager = TaskManager()
    task = manager.add("Learn Git")

    manager.complete(task["id"])

    assert task not in manager.list_tasks("pending")
    assert task in manager.list_tasks("completed")
