# Task Tracker CLI
 A simple command-line tool in Python to help you track your tasks.<br>
 Link : https://roadmap.sh/projects/task-tracker

## Description
Task Tracker CLI is a minimalistic tool for managing tasks directly from the terminal. 
It allows users to add, update, and delete tasks. Users can also  mark a task in-progress or done and list the tasks by status.

## Features
- Add a new task
- Update a task by ID
- Delete a task by ID
- Mark a task as in-progress or done
- List all tasks

## Installation
1. Clone the repository : ```git clone https://github.com/manonlebihan/task-tracker```
2. Navigate to the project folder : ```cd task-tracker```
3. Run it with Python (must be installed) : ```python3 main.py <command> [argument]```

## Usage
#### Add a task
```python3 main.py add task_title```<br>
```python3 main.py add "New task"```

#### Update a task
```python3 main.py update id task_title```<br>
```python3 main.py update 1 "Changing the title"```

#### Delete a task
```python3 main.py delete id```<br>
```python3 main.py delete 1```

#### Mark a as task in-progress or done
```python3 main.py status id```<br>
```python3 main.py done 1```

#### List a tasks (by status or not)
```python3 main.py list [optional_status]```<br>
```python3 main.py list``` or ```python3 main.py list in-progress```
