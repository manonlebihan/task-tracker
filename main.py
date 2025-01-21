from task_manager import load_tasks, add_task, update_task_status_or_title, delete_task, list_tasks
from cli import get_args_parser

def main(file_path="tasks.json"):
    tasks = load_tasks(file_path)
    args = get_args_parser()

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