from .validator import validate_title

class TaskManager:
    def __init__(self, tasks=None):
        self.tasks = list(tasks or [])

    def add(self, title):
        title = validate_title(title)
        task = {"id": len(self.tasks) + 1, "title": title, "completed": False, "priority": "medium"}
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

    def list_tasks(self, status=None):
        if status == "pending":
            return [t for t in self.tasks if not t["completed"]]
        if status == "completed":
            return [t for t in self.tasks if t["completed"]]
        return list(self.tasks)
