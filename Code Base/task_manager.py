"""Daily Task Manager (PS 25) - console based task manager.

Tasks are stored as a list of dictionaries and saved in tasks.txt (JSON text).
Menu: 1 Add, 2 View by priority, 3 Show pending, 4 Complete, 5 Exit
"""

import json
import os
import re
from datetime import datetime

TASK_FILE = "tasks.txt"
PRIORITIES = ["High", "Medium", "Low"]   # also the sorting order
FIRST_ID = 101


# ---------- File handling ----------
def load_tasks(filename=TASK_FILE):
    """Load tasks from file. Missing/empty/corrupt file -> empty list."""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks, filename=TASK_FILE):
    """Save all tasks to file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


# ---------- Validation ----------
def validate_priority(priority):
    """Return normalized priority (High/Medium/Low) or None if invalid."""
    value = priority.strip().capitalize()
    return value if value in PRIORITIES else None


def validate_date(date_text):
    """True only for a real date written exactly as YYYY-MM-DD."""
    date_text = date_text.strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_text):
        return False
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# ---------- Helpers ----------
def generate_id(tasks):
    """Next unique id: T101, T102, ..."""
    numbers = [int(t["id"][1:]) for t in tasks if t["id"][1:].isdigit()]
    return "T{}".format(max(numbers) + 1 if numbers else FIRST_ID)


def format_task(task, show_status=True):
    line = "{} | {} | {} | {}".format(
        task["id"], task["title"], task["priority"], task["due"])
    if show_status:
        line += " | " + task["status"]
    return line


# ---------- Main features (each returns list of output lines) ----------
def add_task(tasks, title, priority, due):
    """Validate and add a task. Priority is checked before date."""
    title = title.strip()
    if not title:
        return ["Title cannot be empty."]
    original_priority = priority
    # Collect errors as (field_was_blank, message).
    # A field that was typed but is wrong is reported first; a blank field
    # is reported only if nothing else is wrong (so each test case in the
    # problem statement, which gives only one field, shows its exact message).
    errors = []
    priority = validate_priority(priority) if priority is not None else None
    if priority is None:
        errors.append((not original_priority.strip(),
                       "Invalid priority. Enter High, Medium or Low."))
    if not validate_date(due):
        errors.append((not due.strip(), "Invalid date. Use YYYY-MM-DD."))
    if errors:
        typed_wrong = [msg for blank, msg in errors if not blank]
        return typed_wrong if typed_wrong else [errors[0][1]]

    task = {"id": generate_id(tasks), "title": title,
            "priority": priority, "due": due.strip(), "status": "Pending"}
    tasks.append(task)
    return ["Task added.", format_task(task)]


def view_by_priority(tasks):
    """List all tasks: High first, then Medium, then Low (by due date)."""
    if not tasks:
        return ["No tasks found."]
    ordered = sorted(tasks, key=lambda t: (PRIORITIES.index(t["priority"]), t["due"]))
    # status is shown only for completed tasks
    return [format_task(t, show_status=False) + (" | Done" if t["status"] == "Done" else "")
            for t in ordered]


def show_pending(tasks):
    pending = [t for t in tasks if t["status"] == "Pending"]
    if not pending:
        return ["No pending tasks. You are all caught up!"]
    return [format_task(t) for t in pending]


def complete_task(tasks, task_id):
    task_id = task_id.strip().upper()
    for t in tasks:
        if t["id"] == task_id:
            if t["status"] == "Done":
                return ["Task {} is already done.".format(task_id)]
            t["status"] = "Done"
            pending = sum(1 for x in tasks if x["status"] == "Pending")
            return ["Task {} marked as done. Pending tasks: {}".format(task_id, pending)]
    return ["Task {} not found.".format(task_id)]


# ---------- Console menu ----------
def print_menu():
    print("\n===== Daily Task Manager =====")
    print("1. Add task")
    print("2. View by priority")
    print("3. Show pending")
    print("4. Complete task")
    print("5. Exit")


def main():
    tasks = load_tasks()
    while True:
        print_menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            title = input("Title: ")
            priority = input("Priority (High/Medium/Low): ")
            due = input("Due date (YYYY-MM-DD): ")
            lines = add_task(tasks, title, priority, due)
            if lines[0] == "Task added.":
                save_tasks(tasks)
        elif choice == "2":
            lines = view_by_priority(tasks)
        elif choice == "3":
            lines = show_pending(tasks)
        elif choice == "4":
            lines = complete_task(tasks, input("Task ID: "))
            if "marked as done" in lines[0]:
                save_tasks(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            lines = ["Invalid choice. Enter 1-5."]
        print("\n".join(lines))


if __name__ == "__main__":
    main()
