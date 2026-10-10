
import argparse

from taskforge.manager import TaskManager
from taskforge.storage import load_tasks, save_tasks
from taskforge.search import search_tasks


PRIORITIES = ["low", "medium", "high"]


def main():
    parser = argparse.ArgumentParser(description="TaskForge CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add")
    add.add_argument("title")
    add.add_argument("--priority", choices=PRIORITIES, default="medium")

    complete = sub.add_parser("complete")
    complete.add_argument("id", type=int)

    delete = sub.add_parser("delete")
    delete.add_argument("id", type=int)

    ls = sub.add_parser("list")
    ls.add_argument("--status", choices=["pending", "completed"])
    ls.add_argument("--priority", choices=PRIORITIES)

    search = sub.add_parser("search")
    search.add_argument("query")

    args = parser.parse_args()
    manager = TaskManager(load_tasks())

    try:
        if args.command == "add":
            print("Added:", manager.add(args.title, args.priority))
        elif args.command == "complete":
            print("Completed:", manager.complete(args.id))
        elif args.command == "delete":
            print("Deleted:", manager.delete(args.id))
        elif args.command == "list":
            for task in manager.list_tasks(args.status, args.priority):
                print(task)
        elif args.command == "search":
            for task in search_tasks(manager.tasks, args.query):
                print(task)

        save_tasks(manager.tasks)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"Error: {exc}\n")


if __name__ == "__main__":
    main()
