#!/usr/bin/env python3
import sys
from task_functions import add_task, list_tasks, update_task, delete_task, change_task_status

# Main function
def main():
    # If no arguments are provided, enter interactive mode
    if len(sys.argv) < 2:
        interactive_mode()
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

# Interface
def interactive_mode():
    print("=== Task Tracker Interactive Mode ===")

    while True:
        print("\nSelect an action:")
        print("1. Add task")
        print("2. List all tasks")
        print("3. List tasks by status")
        print("4. Update task")
        print("5. Delete task")
        print("6. Mark task as in-progress")
        print("7. Mark task as done")
        print("8. Help")
        print("0. Exit")

        choice = input("\nEnter your choice (0-8): ")

        if choice == '0':
            print("Goodbye!")
            break
        elif choice == '1':
            description = input("Enter task description: ")
            task_id = add_task(description)
            print(f"Task added successfully (ID: {task_id})")
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            print("Select status:")
            print("1. Todo")
            print("2. In-progress")
            print("3. Done")
            status_choice = input("Enter choice (1-3): ")
            status_map = {"1": "todo", "2": "in-progress", "3": "done"}
            if status_choice in status_map:
                list_tasks(status_map[status_choice])
            else:
                print("Invalid choice")
        elif choice == '4':
            task_id = input("Enter task ID to update: ")
            description = input("Enter new description: ")
            update_task(task_id, description)
        elif choice == '5':
            task_id = input("Enter task ID to delete: ")
            delete_task(task_id)
        elif choice == '6':
            task_id = input("Enter task ID to mark as in-progress: ")
            change_task_status(task_id, "in-progress")
        elif choice == '7':
            task_id = input("Enter task ID to mark as done: ")
            change_task_status(task_id, "done")
        elif choice == '8':
            print("\nTask Tracker Help:")
            print("1. Add task - Create a new task")
            print("2. List all tasks - Show all tasks regardless of status")
            print("3. List tasks by status - Filter tasks by todo/in-progress/done")
            print("4. Update task - Change the description of a task")
            print("5. Delete task - Remove a task completely")
            print("6. Mark task as in-progress - Change task status to in-progress")
            print("7. Mark task as done - Change task status to done")
            print("0. Exit - Close the application")
        else:
            print("Invalid choice. Please enter a number between 0 and 8.")

if __name__ == "__main__":
    main()