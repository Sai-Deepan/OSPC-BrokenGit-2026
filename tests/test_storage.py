import pytest
from taskforge.storage import load_tasks, save_tasks
def test_load_returns_list_for_missing_file(tmp_path):
    assert load_tasks(tmp_path / "not-here.json") == []
def test_round_trip_preserves_tasks(tmp_path):
    path = tmp_path / "tasks.json"
    tasks = [
        {"id": 1, "title": "Learn Git", "completed": False, "priority": "medium"},
        {"id": 2, "title": "Review PR", "completed": True, "priority": "high"},
    ]
    assert save_tasks(tasks, path) == 2
    assert load_tasks(path) == tasks
def test_malformed_json_raises_clear_error(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_text("{not valid json", encoding="utf-8")
    with pytest.raises(ValueError, match="not valid JSON"):
        load_tasks(path)
def test_wrong_structure_raises_clear_error(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_text('{"id": 1}', encoding="utf-8")
    with pytest.raises(ValueError, match="expected a JSON list"):
        load_tasks(path)
        
