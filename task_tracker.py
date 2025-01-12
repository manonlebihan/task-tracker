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
        "status": "not done",
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
    parser_update = subparsers.add_parser("delete", help="Delete a task")
    parser_update.add_argument("id", type=int, help="ID of the task")

    args = parser.parse_args()
    if args.command == "add":
        add_task(args.title)
    elif args.command == "update":
        update_task(args.id, args.title)
    elif args.command == "delete":
        delete_task(args.id)
    # Call appropriate functions based on `args.command`

main()