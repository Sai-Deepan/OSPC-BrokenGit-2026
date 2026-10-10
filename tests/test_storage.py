import pytest

from taskforge.storage import load_tasks, save_tasks


def test_load_returns_list_for_missing_file(tmp_path):
    assert load_tasks(tmp_path / "not-here.json") == []


def test_save_and_load_round_trip(tmp_path):
    path = tmp_path / "tasks.json"
    tasks = [
        {
            "id": 1,
            "title": "First task",
            "completed": False,
            "priority": "medium",
        },
        {
            "id": 2,
            "title": "Second task",
            "completed": True,
            "priority": "high",
        },
    ]

    assert save_tasks(tasks, path) == 2
    assert load_tasks(path) == tasks


def test_load_malformed_json_raises_actionable_error(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_text('{"id": 1,', encoding="utf-8")

    with pytest.raises(ValueError, match="Invalid JSON") as exc_info:
        load_tasks(path)

    assert str(path) in str(exc_info.value)
    assert "repair" in str(exc_info.value)


def test_load_rejects_non_list_json(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_text('{"id": 1}', encoding="utf-8")

    with pytest.raises(ValueError, match="expected a JSON list"):
        load_tasks(path)
