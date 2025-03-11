# Task Tracker CLI

A simple command-line application to track and manage your tasks.

## Description

Task Tracker is a Python-based CLI application that helps you organize your to-do list by tracking tasks and their status. It stores tasks in a JSON file and provides both command-line and interactive interfaces.

## Features

- Add, update, and delete tasks
- Mark tasks as todo, in-progress, or done
- List all tasks or filter by status
- Command-line interface for scripting
- Interactive mode with menu-driven interface

## Project Structure

The project consists of two main files:

- `task_functions.py`: Contains core functionality (add, list, update, delete tasks)
- `task_cli.py`: Main entry point with CLI and interactive interfaces

Tasks are stored in `tasks.json` in the same directory.

## Installation

1. Download both Python files (`task_functions.py` and `task_cli.py`)
2. Place them in the same directory
3. No external dependencies required - uses only Python standard library

## Usage

### Command-line Interface

```bash
# Adding a new task
python task_cli.py add "Buy groceries"

# Listing tasks
python task_cli.py list
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done

# Updating a task
python task_cli.py update 1 "Buy groceries and medicine"

# Changing task status
python task_cli.py mark-in-progress 1
python task_cli.py mark-done 1

# Deleting a task
python task_cli.py delete 1

# Help
python task_cli.py help
```
## Interactive Mode
Launch without arguments to enter interactive mode:

```bash
python task_cli.py
```
Follow the on-screen menu to perform actions.

## Task Properties
Each task has the following properties:

- id: Unique identifier
- description: Task details
- status: Either "todo", "in-progress", or "done"
- createdAt: Timestamp when the task was created
- updatedAt: Timestamp when the task was last modified

