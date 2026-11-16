# Daily Task Manager

**PS No. 25** | B.Tech Computer Science and Engineering, First Semester
**Rungta International Skills University**, School of Computer Science and Engineering

A Python 3 console application to manage daily tasks. Each task has a title, a priority and a due date. Tasks are saved in a file, so they are still there the next time the program runs.

## Features

- Add a task with title, priority (High / Medium / Low) and due date (YYYY-MM-DD)
- View all tasks sorted by priority (High, then Medium, then Low)
- Show only pending tasks
- Mark a task as done using its Task ID
- Input validation for priority, date format and Task ID
- Auto-generated Task IDs starting from T101
- Tasks are loaded from `tasks.txt` at start and saved after every change

## Concepts Used

Lists, Dictionaries, Functions, File Handling

## Project Structure

```
daily-task-manager/
├── task_manager.py              # Main program
├── README.md                    # Project documentation
├── .gitignore
└── tests/
    ├── test_task_manager.py     # Automated tests (unittest)
    ├── run_test_case_3.py       # Runs Test Case 3 and prints the output
    └── test_cases.md            # Test cases: input and expected output
```

## Requirements

- Python 3.8 or higher
- No external libraries needed

## How to Run

```
python task_manager.py
```

Menu:

```
===== Daily Task Manager =====
1. Add task
2. View by priority
3. Show pending
4. Complete task
5. Exit
```

## Sample Run

```
Enter choice: 1
Title: Submit report
Priority (High/Medium/Low): High
Due date (YYYY-MM-DD): 2026-10-15
Task added.
T101 | Submit report | High | 2026-10-15 | Pending
```

## Test Cases

| # | Type | Input | Expected Output |
|---|------|-------|-----------------|
| 1 | Normal | Add: Submit report, High, 2026-10-15 | `Task added.` and `T101 \| Submit report \| High \| 2026-10-15 \| Pending` |
| 2 | Boundary | No tasks, option 3 | `No pending tasks. You are all caught up!` |
| 3a | Invalid | Add: Pay bill, Priority: Urgent | `Invalid priority. Enter High, Medium or Low.` |
| 3b | Invalid | Add: Pay bill, Due: 15-10-2026 | `Invalid date. Use YYYY-MM-DD.` |
| 3c | Invalid | Option 4: T999 | `Task T999 not found.` |
| 4a | Valid | T101 (High), T102 (Low), T103 (Medium), option 2 | T101, T103, T102 in priority order |
| 4b | Valid | Option 4: T101 | `Task T101 marked as done. Pending tasks: 2` |

Full details are in [`tests/test_cases.md`](tests/test_cases.md).

### Run all tests

```
python -m unittest discover tests -v
```

### Run a single test

```
python tests/test_task_manager.py TestDailyTaskManager.test_case_1_normal_input -v
```

### Run Test Case 3 and see the output

```
python tests/run_test_case_3.py
```

## Notes

- `tasks.txt` is created automatically when the first task is added. It is listed in `.gitignore`, so it is not uploaded to GitHub.
- To start fresh, delete `tasks.txt`.
