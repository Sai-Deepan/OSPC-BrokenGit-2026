
import json
from pathlib import Path

DEFAULT_PATH = Path("tasks.json")


def save_tasks(tasks, path=DEFAULT_PATH):
    path = Path(path)
    path.write_text(
        json.dumps(tasks, indent=2),
        encoding="utf-8"
    )
    return len(tasks)


def load_tasks(path=DEFAULT_PATH):
    path = Path(path)

    if not path.exists():
        return []

    return json.loads(path.read_text(encoding="utf-8"))
