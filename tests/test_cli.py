
import sys

import main


def test_cli_add_with_priority(monkeypatch, capsys):
    saved_tasks = []

    monkeypatch.setattr(main, "load_tasks", lambda: [])
    monkeypatch.setattr(
        main,
        "save_tasks",
        lambda tasks: saved_tasks.extend(tasks),
    )
    monkeypatch.setattr(
        sys,
        "argv",
        ["main.py", "add", "Urgent task", "--priority", "high"],
    )

    main.main()

    assert saved_tasks[0]["title"] == "Urgent task"
    assert saved_tasks[0]["priority"] == "high"
    assert "Added:" in capsys.readouterr().out


def test_cli_list_filters_by_priority(monkeypatch, capsys):
    tasks = [
        {
            "id": 1,
            "title": "Low task",
            "completed": False,
            "priority": "low",
        },
        {
            "id": 2,
            "title": "High task",
            "completed": False,
            "priority": "high",
        },
    ]

    monkeypatch.setattr(main, "load_tasks", lambda: tasks)
    monkeypatch.setattr(main, "save_tasks", lambda tasks: None)
    monkeypatch.setattr(
        sys,
        "argv",
        ["main.py", "list", "--priority", "high"],
    )

    main.main()

    output = capsys.readouterr().out
    assert "High task" in output
    assert "Low task" not in output


def test_cli_rejects_unsupported_priority(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["main.py", "add", "Bad task", "--priority", "urgent"],
    )

    try:
        main.main()
    except SystemExit as exc:
        assert exc.code == 2
    else:
        raise AssertionError("Expected invalid priority to be rejected")
