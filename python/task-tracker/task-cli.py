#!/usr/bin/env python3
import json
import sys
import os
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

# Function to read tasks from the JSON file
def read_tasks():
    if not os.path.exists(TASKS_FILE):
        return []

    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

# Function to write tasks to the JSON file
def write_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

# Function to add a new task
def add_task(description):
    tasks = read_tasks()

    # Generate new task ID (max ID + 1, or 1 if no tasks exist)
    task_id = 1
    if tasks:
        task_id = max(task["id"] for task in tasks) + 1

    # Create timestamp for creation/update time
    timestamp = datetime.now().isoformat()

    # Create new task object
    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": timestamp,
        "updatedAt": timestamp
    }

    # Add to tasks list and save
    tasks.append(new_task)
    write_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

# Function to list tasks
def list_tasks(status_filter=None):
    tasks = read_tasks()

    if not tasks:
        print("No tasks found.")
        return

    # Filter tasks by status if a filter is provided
    if status_filter:
        filtered_tasks = [task for task in tasks if task["status"] == status_filter]

        if not filtered_tasks:
            print(f"No tasks with status '{status_filter}' found.")
            return

        tasks = filtered_tasks

    # Print tasks in a formatted way
    print(f"{'ID':<5} {'Status':<12} {'Description':<50}")
    print("-" * 67)

    for task in tasks:
        print(f"{task['id']:<5} {task['status']:<12} {task['description']}")

# Function to update a task
def update_task(task_id, new_description):
    tasks = read_tasks()
    task_id = int(task_id)  # Convert to integer

    # Find the task by ID
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            write_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return

    print(f"Task with ID {task_id} not found")

# Function to delete a task
def delete_task(task_id):
    tasks = read_tasks()
    task_id = int(task_id)  # Convert to integer

    # Find the task by ID and remove it
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            write_tasks(tasks)
            print(f"Task {task_id} deleted successfully")
            return

    print(f"Task with ID {task_id} not found")

# Function to change task status
def change_task_status(task_id, new_status):
    tasks = read_tasks()
    task_id = int(task_id)  # Convert to integer

    # Find the task by ID
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            write_tasks(tasks)
            print(f"Task {task_id} marked as '{new_status}' successfully")
            return

    print(f"Task with ID {task_id} not found")

# Main function
def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [options]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py add <description>")
            return
        add_task(sys.argv[2])

    elif command == "list":
        # Handle list command with optional status filter
        if len(sys.argv) == 2:
            # List all tasks
            list_tasks()
        elif len(sys.argv) == 3:
            # List tasks by status
            status = sys.argv[2]
            # Map command line arguments to actual status values
            status_map = {
                "todo": "todo",
                "in-progress": "in-progress",
                "done": "done"
            }
            if status in status_map:
                list_tasks(status_map[status])
            else:
                print(f"Invalid status filter: {status}")

    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: python task_cli.py update <task_id> <new_description>")
            return
        update_task(sys.argv[2], sys.argv[3])

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py delete <task_id>")
            return
        delete_task(sys.argv[2])

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py mark-in-progress <task_id>")
            return
        change_task_status(sys.argv[2], "in-progress")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py mark-done <task_id>")
            return
        change_task_status(sys.argv[2], "done")

    elif command == "help":
        print("Task Tracker CLI - Available commands:")
        print("add <description>           - Add a new task")
        print("list                        - List all tasks")
        print("list <status>               - List tasks by status (todo, in-progress, done)")
        print("update <id> <description>   - Update task description")
        print("delete <id>                 - Delete a task")
        print("mark-in-progress <id>       - Mark task as in progress")
        print("mark-done <id>              - Mark task as done")
        print("help                        - Show this help message")

    else:
        print(f"Unknown command: {command}")
        print("Use 'python task_cli.py help' to see available commands")

if __name__ == "__main__":
    main()

    