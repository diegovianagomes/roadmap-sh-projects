import json
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