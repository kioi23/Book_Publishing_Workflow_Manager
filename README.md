# Book Publishing Workflow Manager

A simple Python command-line application for managing the publishing workflow of books, authors, editors, and editorial tasks. The app uses a JSON file for persistence, so data is saved between runs without requiring a database server.

## Features

- Add and list authors
- Add and list editors
- Add and list books
- Add, list, complete, and update editorial tasks
- Assign an editor to a book
- Update a book milestone
- Add and view feedback for a task

## Project Structure

```text
main.py
README.md
requirements.txt
data/
	database.json
models/
	author.py
	book.py
	editor.py
	person.py
	task.py
utils/
	helpers.py
	storage.py
tests/
	test_author.py
	test_book.py
	test_task.py
```

## Requirements

- Python 3
- `pip`

The project uses `rich` for formatted CLI output. If you want to run tests, install `pytest` separately or add it to your environment.

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the dependencies.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the CLI

All commands are run from the project root.

```bash
python main.py <command> [options]
```

### Authors

Add an author:

```bash
python main.py add-author --name "Bruce James" --email "bruce@gmail.com"
```

List authors:

```bash
python main.py list-authors
```

### Editors

Add an editor:

```bash
python main.py add-editor --name "Kioi" --email "kioi@gmail.com"
```

List editors:

```bash
python main.py list-editors
```

### Books

Add a book:

```bash
python main.py add-book --title "Wealth Of Nations" --genre "Economics" --author "Bruce James"
```

List books:

```bash
python main.py list-books
```

Assign an editor to a book:

```bash
python main.py assign-editor --book "Wealth Of Nations" --editor "Kioi"
```

Update a book milestone:

```bash
python main.py update-milestone --book "Wealth Of Nations" --milestone Editing
```

Valid milestones are:

- `Draft`
- `Editing`
- `Review`
- `Published`

### Tasks

Add a task:

```bash
python main.py add-task --title "Chapter 1 Revision" --editor "Kioi"
```

List tasks:

```bash
python main.py list-tasks
```

Complete a task:

```bash
python main.py complete-task --title "Chapter 1 Revision"
```

Add feedback to a task:

```bash
python main.py add-feedback --task "Chapter 1 Revision" --feedback "Rewrite introduction and fix grammar."
```

View task feedback:

```bash
python main.py view-feedback --task "Chapter 1 Revision"
```

## Data Storage

The application stores data in [data/database.json](data/database.json). The file contains four top-level collections:

- `authors`
- `editors`
- `books`
- `tasks`

The CLI matches records by exact string values such as author names, editor names, book titles, and task titles. If a name or title does not match exactly, the command reports that the record was not found.

## Notes

- Books start at the `Draft` milestone.
- Tasks start with a `Pending` status.
- Adding a task initializes its feedback as an empty string.
- If `data/database.json` is missing, the app recreates in-memory data structures automatically when commands run.

## Testing

The repository includes a `tests/` directory prepared for `pytest`. If `pytest` is installed, run tests with:
```bash
pytest
```

At the moment, the visible test files are scaffolds, so test coverage is still a work in progress.

## Example Workflow

```bash
python main.py add-author --name "Bruce James" --email "bruce@gmail.com"
python main.py add-editor --name "Kioi" --email "kioi@gmail.com"
python main.py add-book --title "Wealth Of Nations" --genre "Economics" --author "Bruce James"
python main.py assign-editor --book "Wealth Of Nations" --editor "Kioi"
python main.py update-milestone --book "Wealth Of Nations" --milestone Editing
python main.py add-task --title "Chapter 1 Revision" --editor "Kioi"
python main.py add-feedback --task "Chapter 1 Revision" --feedback "Rewrite introduction and fix grammar."
python main.py complete-task --title "Chapter 1 Revision"
```

## Troubleshooting

- Make sure the virtual environment is activated before running commands.
- Run commands from the project root so `data/database.json` is found correctly.
- Use exact names and titles when referencing records.
