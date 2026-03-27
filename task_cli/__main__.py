import argparse
from task_cli.tasktracker import TaskTracker

def main():
    tasktracker = TaskTracker()

    parser = argparse.ArgumentParser(description="A CLI Task Tracker Tool", epilog="Example: task-cli add \"Do the dishes\"")

    subparsers = parser.add_subparsers(title="Commands", dest="command")

    add_parser = subparsers.add_parser("add", help="Add task")
    add_parser.add_argument("description", type=str, help="Task description")

    update_parser = subparsers.add_parser("update", help="Update task")
    update_parser.add_argument("id", type=str, help="Task id")
    update_parser.add_argument("description", type=str, help="Task description")

    delete_parser = subparsers.add_parser("delete", help="Delete task by id")
    delete_parser.add_argument("id", type=str, help="Task id")

    mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Mark task in progress")
    mark_in_progress_parser.add_argument("id", type=str, help="Task id")

    mark_done_parser = subparsers.add_parser("mark-done", help="Mark task done")
    mark_done_parser.add_argument("id", type=str, help="Task id")

    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("filter", type=str, help="Filter", default="", nargs="?")

    args = parser.parse_args()

    if args.command == "add":
        tasktracker.add(args.description)
        print(f"Added '{args.description}' to list")
    elif args.command == "update":
        tasktracker.update(args.id, args.description)
        print(f"Updated '{args.id}' to '{args.description}'")
    elif args.command == "delete":
        tasktracker.delete(args.id)
        print(f"Deleted '{args.id}' from list")
    elif args.command == "mark-in-progress":
        tasktracker.update_status(args.id, "in-progress")
        print(f"Marked '{args.id}' in progress")
    elif args.command == "mark-done":
        tasktracker.update_status(args.id, "done")
        print(f"Marked '{args.id}' done")
    elif args.command == "list":
        result = tasktracker._list(args.filter)
        for task in result:
            print(f"{task['id']}\t{task['description']}\t{task['status']}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()