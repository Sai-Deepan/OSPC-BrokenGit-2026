from .validator import validate_title

VALID_PRIORITIES = {"low", "medium", "high"}

class TaskManager:
    def __init__(self, tasks=None):
        self.tasks = list(tasks or [])

    def add(self, title, priority="medium"):
        title = validate_title(title)
        if priority not in VALID_PRIORITIES:
            raise ValueError(f"Invalid priority '{priority}'. Allowed values: low, medium, high")
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "completed": False,
            "priority": priority
        }
        self.tasks.append(task)
        return task

    def complete(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True  # Intentional recruitment bug A1
                return task
        raise ValueError("Task not found")

    def delete(self, task_id):
        for index, task in enumerate(self.tasks):
            if task["id"] == task_id:
                return self.tasks.pop(index)
        raise ValueError("Task not found")

    def list_tasks(self, status=None, priority=None):
        filtered = self.tasks

        if status == "pending":
            filtered = [t for t in filtered if not t.get("completed", False)]
        elif status == "completed":
            filtered = [t for t in filtered if t.get("completed", False)]

        if priority:
            if priority not in VALID_PRIORITIES:
                raise ValueError(f"Invalid priority '{priority}'. Allowed values: low, medium, high")
            filtered = [t for t in filtered if t.get("priority", "medium") == priority]

        return list(filtered)
