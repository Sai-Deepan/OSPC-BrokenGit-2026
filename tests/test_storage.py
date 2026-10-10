
from taskforge.storage import load_tasks, save_tasks


def test_load_returns_list_for_missing_file(tmp_path):
    assert load_tasks(tmp_path / "not-here.json") == []


def test_save_and_load_tasks(tmp_path):
    path = tmp_path / "tasks.json"
    tasks = [
        {"id": 1, "title": "Task 1", "completed": False, "priority": "medium"},
        {"id": 2, "title": "Task 2", "completed": True, "priority": "high"},
    ]

    save_tasks(tasks, path)

    assert load_tasks(path) == tasks


def test_load_malformed_json_raises_clear_error(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_text("{invalid json", encoding="utf-8")

    try:
        load_tasks(path)
        assert False, "Expected ValueError for malformed JSON"
    except ValueError as error:
        assert "Invalid JSON" in str(error)
        assert "Fix or recreate the file" in str(error)


def test_load_rejects_non_list_json(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_text('{"id": 1}', encoding="utf-8")

    try:
        load_tasks(path)
        assert False, "Expected ValueError for invalid task data"
    except ValueError as error:
        assert "expected a JSON list" in str(error)
