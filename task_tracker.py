import json
import os
import argparse
from datetime import datetime

file_path = "tasks.json"

def load_tasks(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump([], f)
    with open(file_path, 'r') as f:
        return json.load(f)

def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_tasks(tasks, file_path):
    with open(file_path, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(title, file_path=file_path):
    tasks = load_tasks(file_path)

    next_id = max([task["id"] for task in tasks], default=0) + 1

    current_time = get_current_timestamp()
    new_task = {
        "id": next_id,
        "title": title,
        "status": "todo",
        "createdAt": current_time,
        "updatedAt": current_time
    }

    tasks.append(new_task)
    save_tasks(tasks, file_path)

    print(f"Task added successfully (ID {next_id}): {title}")

def update_task(task_id, new_title, file_path=file_path):
    tasks = load_tasks(file_path="tasks.json")

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = new_title
            task["updatedAt"] = get_current_timestamp()
            save_tasks(tasks, file_path)
            print(f"Task with ID {task_id} was updated")
            return
    print(f"Task with ID {task_id} not found")

def delete_task(task_id, file_path=file_path):
    tasks = load_tasks(file_path)

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks, file_path)
            print(f"Task with ID {task_id} was deleted")
            return
    print(f"Task with ID {task_id} not found")

def mark_task_in_progress(task_id, file_path=file_path):
    tasks = load_tasks(file_path)

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = get_current_timestamp()
            save_tasks(tasks, file_path)
            print(f"Task with ID {task_id} was marked 'in-progress'")
            return
    print(f"Task with ID {task_id} not found")

def mark_task_done(task_id, file_path=file_path):
    tasks = load_tasks(file_path)

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = get_current_timestamp()
            save_tasks(tasks, file_path)
            print(f"Task with ID {task_id} was marked 'done'")
            return
    print(f"Task with ID {task_id} not found")

def list_task(status_filter, file_path=file_path):
    tasks = load_tasks(file_path)

    for task in tasks:
        if status_filter != "all" and task["status"] != status_filter:
            continue
        print(f"{task['title']}, status: {task['status']}")

def main():
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

    args = parser.parse_args()
    if args.command == "add":
        add_task(args.title)
    elif args.command == "update":
        update_task(args.id, args.title)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "mark-in-progress":
        mark_task_in_progress(args.id)
    elif args.command == "mark-done":
        mark_task_done(args.id)
    elif args.command == "list":
        list_task(status_filter=args.status)

main()