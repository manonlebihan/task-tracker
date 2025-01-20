import json
import os
import argparse
from datetime import datetime

def load_tasks(file_path):
    if not os.path.exists(file_path): # is this necessary
        with open(file_path, 'w') as f:
            json.dump([], f)
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: tasks.json is corrupted. Resetting file.")
        with open(file_path, 'w') as f:
            json.dump([], f)
        return[]

def save_tasks(tasks, file_path):
    with open(file_path, 'w') as f:
        json.dump(tasks, f, indent=4)

def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def add_task(title, tasks, file_path):
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

def update_task_status_or_title(task_id, tasks, file_path, title=None, status=None):
   if not any(task["id"] == task_id for task in tasks):
       print(f"Error: No task found with ID {task_id}")
       return

   for task in tasks:
        if task["id"] == task_id:
            if title:
                task["title"] = title
            if status:
                task["status"] = status
            task["updatedAt"] = get_current_timestamp()
            save_tasks(tasks, file_path)
            print(f"Task with ID {task_id} was updated")
            return

def delete_task(task_id, tasks, file_path):
    if not any(task["id"] == task_id for task in tasks):
       print(f"Error: No task found with ID {task_id}")
       return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks, file_path)
            print(f"Task with ID {task_id} was deleted")
            return

def list_tasks(status_filter, tasks):
    filtered_tasks = [task for task in tasks if status_filter == "all" or task["status"] == status_filter]

    if filtered_tasks:
        for task in filtered_tasks:
            print(f"ID {task['id']}: {task['title']} (Status: {task['status']})")
    else:
        print(f"No task with the {status_filter} status have been found")

def parser():
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

def main(file_path="tasks.json"):
    tasks = load_tasks(file_path)
    args = parser()

    if args.command == "add":
        add_task(args.title, tasks, file_path)
    elif args.command == "update":
        update_task_status_or_title(args.id, tasks, file_path, title=args.title)
    elif args.command == "delete":
        delete_task(args.id, tasks, file_path)
    elif args.command == "mark-in-progress":
        update_task_status_or_title(args.id, tasks, file_path, status="in-progress")
    elif args.command == "mark-done":
        update_task_status_or_title(args.id, tasks, file_path, status="done")
    elif args.command == "list":
        list_tasks(args.status, tasks)

main()

update_task_status_or_title
delete_task
list_tasks