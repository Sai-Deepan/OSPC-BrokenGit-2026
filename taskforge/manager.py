from .validator import validate_title

class TaskManager:
    def __init__(self, tasks=None):
        self.tasks = list(tasks or [])
        self._next_id = max(
        (task["id"] for task in self.tasks),
        default=0
    ) + 1

    def add(self, title):
        title = validate_title(title)

        task = {
            "id": self._next_id,
            "title": title,
            "completed": False,
            "priority": "medium"
        }

        self.tasks.append(task)
        self._next_id += 1

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

    def list_tasks(self, status=None):
        if status == "pending":
            return [t for t in self.tasks if not t["completed"]]
        if status == "completed":
            return [t for t in self.tasks if t["completed"]]
        return list(self.tasks)
