from .validator import validate_title

class TaskManager:
    VALID_PRIORITIES = {"low", "medium", "high"}

    def __init__(self, tasks=None):
        self.tasks = []
        for task in (tasks or []):
            t = dict(task)
            if "priority" not in t:
                t["priority"] = "medium"
            self.tasks.append(t)

    def add(self, title, priority="medium"):
        title = validate_title(title)
        if priority not in self.VALID_PRIORITIES:
            raise ValueError(f"Invalid priority: {priority}. Must be one of {sorted(self.VALID_PRIORITIES)}")
        next_id = max((task["id"] for task in self.tasks), default=0) + 1
        task = {"id": next_id, "title": title, "completed": False, "priority": priority}
        self.tasks.append(task)
        return task

    def complete(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return task
        raise ValueError("Task not found")

    def delete(self, task_id):
        for index, task in enumerate(self.tasks):
            if task["id"] == task_id:
                return self.tasks.pop(index)
        raise ValueError("Task not found")

    def list_tasks(self, status=None, priority=None):
        results = self.tasks
        if status == "pending":
            results = [t for t in results if not t.get("completed", False)]
        elif status == "completed":
            results = [t for t in results if t.get("completed", False)]

        if priority is not None:
            if priority not in self.VALID_PRIORITIES:
                raise ValueError(f"Invalid priority: {priority}. Must be one of {sorted(self.VALID_PRIORITIES)}")
            results = [t for t in results if t.get("priority", "medium") == priority]
        return list(results)

