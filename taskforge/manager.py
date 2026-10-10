from .validator import validate_title

VALID_PRIORITIES = {"low", "medium", "high"}


def validate_priority(priority):
    if priority not in VALID_PRIORITIES:
        raise ValueError(
            f"Invalid priority: {priority}. Choose low, medium, or high."
        )
    return priority


class TaskManager:
    def __init__(self, tasks=None):
        self.tasks = list(tasks or [])

    def add(self, title, priority="medium"):
        title = validate_title(title)
        priority = validate_priority(priority)

        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "completed": False,
            "priority": priority,
        }
        self.tasks.append(task)
        return task

    def complete(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                return task
        raise ValueError("Task not found")

    def delete(self, task_id):
        for index, task in enumerate(self.tasks):
            if task["id"] == task_id:
                return self.tasks.pop(index)
        raise ValueError("Task not found")

    def list_tasks(self, status=None, priority=None):

        if priority is not None:
            priority = validate_priority(priority)

        tasks = self.tasks

        if status == "pending":
            tasks = [task for task in tasks if not task["completed"]]
        elif status == "completed":
            tasks = [task for task in tasks if task["completed"]]

        if priority is not None:
            # Older tasks without a priority are treated as medium.
            tasks = [
                task for task in tasks
                if task.get("priority", "medium") == priority
            ]

        return list(tasks)
