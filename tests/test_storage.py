import json
import pytest
from taskforge.storage import load_tasks, save_tasks


def test_save_and_load_tasks_round_trip(tmp_path):
    path = tmp_path / "tasks.json"
    tasks = [
        {
            "id": 1,
            "title": "Learn JSON",
            "completed": False,
            "priority": "high",
        }
    ]

    assert save_tasks(tasks, path) == 1
    assert load_tasks(path) == tasks


def test_load_returns_empty_list_for_missing_file(tmp_path):
    assert load_tasks(tmp_path / "missing.json") == []


def test_load_malformed_json_raises_actionable_error(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_text('{"tasks": ', encoding="utf-8")

    with pytest.raises(ValueError, match="Fix or delete the file"):
        load_tasks(path)


def test_load_rejects_json_that_is_not_a_list(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_text(json.dumps({"task": "Learn JSON"}), encoding="utf-8")

    with pytest.raises(ValueError, match="expected a JSON list"):
        load_tasks(path)
