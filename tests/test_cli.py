import json
from pathlib import Path
import subprocess
import sys


CLI_PATH = Path(__file__).resolve().parents[1] / "main.py"


def run_cli(workdir, *args):
    return subprocess.run(
        [sys.executable, str(CLI_PATH), *args],
        cwd=workdir,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


def test_task_survives_separate_cli_processes(tmp_path):
    added = run_cli(tmp_path, "add", "Learn persistent storage")
    listed = run_cli(tmp_path, "list")

    assert added.returncode == 0, added.stderr
    assert listed.returncode == 0, listed.stderr
    assert "Learn persistent storage" in listed.stdout
    assert json.loads((tmp_path / "tasks.json").read_text(encoding="utf-8")) == [
        {"id": 1, "title": "Learn persistent storage", "completed": False, "priority": "medium"}
    ]


def test_deleting_last_task_stays_deleted_after_restart(tmp_path):
    assert run_cli(tmp_path, "add", "Delete me").returncode == 0
    deleted = run_cli(tmp_path, "delete", "1")
    listed = run_cli(tmp_path, "list")

    assert deleted.returncode == 0, deleted.stderr
    assert listed.returncode == 0, listed.stderr
    assert listed.stdout == ""
    assert json.loads((tmp_path / "tasks.json").read_text(encoding="utf-8")) == []


def test_malformed_storage_reports_error_without_overwriting_file(tmp_path):
    path = tmp_path / "tasks.json"
    contents = "{broken json}"
    path.write_text(contents, encoding="utf-8")

    result = run_cli(tmp_path, "add", "Do not overwrite broken storage")

    assert result.returncode == 1
    assert "Error:" in result.stderr
    assert "invalid JSON" in result.stderr
    assert "Fix the file or move it aside" in result.stderr
    assert "Traceback" not in result.stderr
    assert result.stdout == ""
    assert path.read_text(encoding="utf-8") == contents


def test_storage_io_error_is_reported_without_traceback(tmp_path):
    (tmp_path / "tasks.json").mkdir()

    result = run_cli(tmp_path, "list")

    assert result.returncode == 1
    assert "Error:" in result.stderr
    assert "Traceback" not in result.stderr
