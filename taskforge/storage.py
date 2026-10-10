import json
from pathlib import Path

DEFAULT_PATH = Path("tasks.json")


def save_tasks(tasks, path=DEFAULT_PATH):
    path = Path(path)
    with path.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)
    return len(tasks)


def load_tasks(path=DEFAULT_PATH):
    path = Path(path)

    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as file:
        tasks = json.load(file)

    if not isinstance(tasks, list):
        raise ValueError("Stored tasks must be a JSON list")

    return tasks