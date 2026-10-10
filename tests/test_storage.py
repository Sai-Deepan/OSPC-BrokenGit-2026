import json

import pytest

from taskforge.storage import load_tasks, save_tasks

def test_load_returns_list_for_missing_file(tmp_path):
    assert load_tasks(tmp_path / "not-here.json") == []


def test_tasks_round_trip_without_losing_fields(tmp_path):
    path = tmp_path / "tasks.json"
    tasks = [
        {"id": 1, "title": "Learn Python 🐍", "completed": False, "priority": "high"},
        {"id": 2, "title": "  Read தமிழ் notes  ", "completed": True},
    ]

    assert save_tasks(tasks, path) == 2
    assert json.loads(path.read_text(encoding="utf-8")) == tasks
    assert load_tasks(path) == tasks


def test_empty_task_list_round_trips_with_string_path(tmp_path):
    path = str(tmp_path / "empty.json")

    assert save_tasks([], path) == 0
    assert load_tasks(path) == []


def test_saving_replaces_previous_tasks(tmp_path):
    path = tmp_path / "tasks.json"
    save_tasks([{"id": 1, "title": "Delete me", "completed": False}], path)

    save_tasks([], path)

    assert json.loads(path.read_text(encoding="utf-8")) == []
    assert load_tasks(path) == []


@pytest.mark.parametrize("contents", ["", "{not json}", '[{"id": 1,}]'])
def test_malformed_json_has_actionable_error_and_is_preserved(tmp_path, contents):
    path = tmp_path / "broken.json"
    path.write_text(contents, encoding="utf-8")

    with pytest.raises(ValueError, match="invalid JSON") as error:
        load_tasks(path)

    assert str(path) in str(error.value)
    assert "Fix the file or move it aside" in str(error.value)
    assert path.read_text(encoding="utf-8") == contents


@pytest.mark.parametrize("contents", ["null", "{}", "42", '"tasks"'])
def test_json_must_contain_a_task_list(tmp_path, contents):
    path = tmp_path / "tasks.json"
    path.write_text(contents, encoding="utf-8")

    with pytest.raises(ValueError, match="JSON list"):
        load_tasks(path)

    assert path.read_text(encoding="utf-8") == contents


def test_invalid_utf8_has_actionable_error(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_bytes(b"\xff")

    with pytest.raises(ValueError, match="invalid JSON"):
        load_tasks(path)

    assert path.read_bytes() == b"\xff"
