import subprocess
import sys
import json
from pathlib import Path

MAIN_SCRIPT = str(Path(__file__).resolve().parent.parent / "main.py")

def run_cli(*args, cwd=None):
    return subprocess.run(
        [sys.executable, MAIN_SCRIPT, *args],
        capture_output=True,
        text=True,
        cwd=cwd
    )

def test_cli_add_and_list(tmp_path, monkeypatch):
    # Run with tasks file in tmp_path by executing in tmp_path
    tasks_file = tmp_path / "tasks.json"
    result = run_cli("add", "CLI Test Task", "--priority", "high", cwd=tmp_path)
    assert result.returncode == 0
    assert "Added:" in result.stdout
    assert "CLI Test Task" in result.stdout

    # List
    list_res = run_cli("list", "--priority", "high", cwd=tmp_path)
    assert list_res.returncode == 0
    assert "CLI Test Task" in list_res.stdout

def test_cli_complete_and_delete(tmp_path):
    run_cli("add", "Task to Complete", cwd=tmp_path)
    comp_res = run_cli("complete", "1", cwd=tmp_path)
    assert comp_res.returncode == 0
    assert "'completed': True" in comp_res.stdout

    del_res = run_cli("delete", "1", cwd=tmp_path)
    assert del_res.returncode == 0
    assert "Deleted:" in del_res.stdout

def test_cli_search(tmp_path):
    run_cli("add", "Learn Python and Git", cwd=tmp_path)
    search_res = run_cli("search", "python", cwd=tmp_path)
    assert search_res.returncode == 0
    assert "Learn Python and Git" in search_res.stdout

def test_cli_invalid_command_error():
    res = run_cli("add", "   ")
    assert res.returncode != 0
    assert "Error:" in res.stderr
