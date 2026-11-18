# Task Tracker — Software Engineering Practice

A command-line task tracker built in Python as a hands-on software engineering practice project.

The application lets a user create tasks, view the task list, mark tasks as complete, and delete tasks. It stores task data in a local JSON file so tasks remain available after the program is closed and restarted.

## Features

- **Add tasks:** Accepts a task description and rejects empty input.
- **View tasks:** Lists tasks with a numbered position and a `Pending` or `Done` status.
- **Complete tasks:** Marks a selected task as complete.
- **Delete tasks:** Removes a selected task from the list.
- **Input validation:** Handles invalid menu choices, non-numeric task selections, and task numbers outside the valid range.
- **Persistent storage:** Loads tasks from `tasks.json` at startup and saves changes after additions, completions, and deletions.
- **JSON validation:** Uses Python's JSON tooling to verify that the saved data is valid JSON.

## Technologies

- Python 3
- Python standard library: `json` and `os`
- JSON for local data storage
- Terminal / command-line interface

No third-party packages are required.

## Run the application

From this project directory, run:

```bash
python3 task_tracker.py
```

The application creates or updates `tasks.json` in the current working directory when task data is saved.

## Menu

```text
1. Add task
2. View tasks
3. Complete task
4. Delete task
5. Exit
```

## Verification performed

The application was manually exercised in the terminal. The following behaviors were observed:

| Check | Result |
| --- | --- |
| View an empty task list | Passed |
| Add and display a task | Passed |
| Reject an empty task description | Passed |
| Handle an invalid menu selection | Passed |
| Mark a task as completed and display `Done` | Passed |
| Delete a task and confirm the list is empty | Passed |
| Handle deletion when the list is empty | Passed |
| Reject a task number outside the valid range | Passed |
| Handle non-numeric input for completion and deletion | Passed |
| Save a task, exit, restart, and load the task again | Passed |
| Validate the saved file with `python3 -m json.tool tasks.json` | Passed |

These are manual checks, not an automated unit-test suite.

## Project structure

```text
software-engineering-task-tracker/
├── README.md
└── task_tracker.py
```

The `tasks.json` file is generated locally when the application saves its first task; it is runtime data rather than part of the source code.

## Skills demonstrated

This practice project demonstrates:

- Breaking a program into functions with distinct responsibilities
- Working with lists and dictionaries
- Using conditionals and loops to control program behavior
- Validating user input and handling `ValueError`
- Reading and writing structured JSON data
- Separating application logic into reusable functions
- Manually testing expected behavior and edge cases

## Current limitations

- Tasks are stored locally on the machine running the program.
- There is no graphical interface, database, or multi-user support.
- The application has manual verification notes but no automated test suite yet.

## Next improvements

Potential future improvements include automated unit tests, safer recovery from a damaged JSON file, and separating storage logic from the command-line interface.
