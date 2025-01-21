import argparse

def get_args_parser():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add task
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("title", type=str, help="Title of the task")

    # Update task
    parser_update = subparsers.add_parser("update", help="Update a task")
    parser_update.add_argument("id", type=int, help="ID of the task")
    parser_update.add_argument("title", type=str, help="New title of the task")

    # Delete task
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="ID of the task")

    # Mark a task as in-progress
    parser_in_progress = subparsers.add_parser("mark-in-progress", help="Mark a task as in progress")
    parser_in_progress.add_argument("id", type=int, help="ID of the task")

    # Mark a task as done
    parser_done = subparsers.add_parser("mark-done", help="Mark a task as done")
    parser_done.add_argument("id", type=int, help="ID of the task")

    # Listing all tasks (by status or not)
    parser_list = subparsers.add_parser("list", help="List all the tasks")
    parser_list.add_argument("status", type=str, choices=["done", "in-progress", "todo", "all"], nargs="?", default="all", help="Filter tasks by status (done, in-progress, todo, or all)")

    return parser.parse_args()