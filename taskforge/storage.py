import json
from pathlib import Path

DEFAULT_PATH = Path("tasks.json")

def save_tasks(tasks, path=DEFAULT_PATH):
    """Write the task list as UTF-8 JSON and return the number saved."""
    Path(path).write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return len(tasks)

def load_tasks(path=DEFAULT_PATH):
    """Load saved tasks; only a missing file starts a new empty list."""
    path = Path(path)
    try:
        tasks = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise ValueError(
            f"Cannot load tasks from '{path}': invalid JSON. "
            "Fix the file or move it aside to start with an empty task list."
        ) from exc

    if not isinstance(tasks, list):
        raise ValueError(
            f"Cannot load tasks from '{path}': expected a JSON list of tasks. "
            "Fix the file or move it aside to start with an empty task list."
        )
    return tasks
