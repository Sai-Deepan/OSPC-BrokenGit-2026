
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

    try:
        with path.open("r", encoding="utf-8") as file:
            tasks = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid JSON in {path}. Fix or recreate the file."
        ) from error

    if not isinstance(tasks, list):
        raise ValueError(
            f"Invalid task data in {path}: expected a JSON list."
        )

    return tasks
