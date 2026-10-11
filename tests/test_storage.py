from taskforge.storage import load_tasks, save_tasks

def test_load_returns_list_for_missing_file(tmp_path):
    assert load_tasks(tmp_path / "not-here.json") == []

def test_save_and_load_tasks(tmp_path):
    file_path = tmp_path / "tasks.json"
    tasks = [{"id": 1, "title": "Test Task", "completed": False, "priority": "medium"}]
    count = save_tasks(tasks, file_path)
    assert count == 1
    loaded = load_tasks(file_path)
    assert loaded == tasks

def test_load_empty_file(tmp_path):
    file_path = tmp_path / "empty.json"
    file_path.write_text("")
    assert load_tasks(file_path) == []

def test_save_creates_nested_directories(tmp_path):
    nested_path = tmp_path / "deep" / "nested" / "tasks.json"
    tasks = [{"id": 1, "title": "Nested", "completed": False, "priority": "low"}]
    assert save_tasks(tasks, nested_path) == 1
    assert load_tasks(nested_path) == tasks

def test_save_empty_list(tmp_path):
    file_path = tmp_path / "tasks.json"
    assert save_tasks([], file_path) == 0
    assert load_tasks(file_path) == []

def test_save_overwrites_existing_file(tmp_path):
    file_path = tmp_path / "tasks.json"
    save_tasks([{"id": 1, "title": "Old", "completed": False, "priority": "low"}], file_path)
    save_tasks([{"id": 2, "title": "New", "completed": True, "priority": "high"}], file_path)
    loaded = load_tasks(file_path)
    assert len(loaded) == 1
    assert loaded[0]["title"] == "New"


