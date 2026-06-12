import argparse

from models.author import Author
from models.book import Book
from models.editor import Editor
from utils.storage import load_data, save_data
from rich import print

# Create parser
parser = argparse.ArgumentParser(
    description="Book Publishing Workflow Manager"
)

# Create subcommands
subparsers = parser.add_subparsers(dest="command")

# ADD AUTHOR COMMAND

author_parser = subparsers.add_parser(
    "add-author",
    help="Add a new author"
)

author_parser.add_argument(
    "--name",
    required=True
)

author_parser.add_argument(
    "--email",
    required=True
)


# ADD BOOK COMMAND

book_parser = subparsers.add_parser(
    "add-book",
    help="Add a new book"
)

book_parser.add_argument(
    "--title",
    required=True
)

book_parser.add_argument(
    "--genre",
    required=True
)

book_parser.add_argument(
    "--author",
    required=True
)

#ADD EDITOR COMMAND

editor_parser = subparsers.add_parser(
    "add-editor",
    help="Add a new editor"
)

editor_parser.add_argument(
    "--name",
    required=True
)

editor_parser.add_argument(
    "--email",
    required=True
)

    # List Authors Command
list_authors_parser = subparsers.add_parser(
    "list-authors",
    help="Display all authors"
    )

# LIST EDITORS COMMAND

list_editors_parser = subparsers.add_parser(
    "list-editors",
    help="Display all editors"
)

# LIST BOOKS COMMAND

list_books_parser = subparsers.add_parser(
    "list-books",
    help="Display all books"
)

# ADD TASK COMMAND

task_parser = subparsers.add_parser(
    "add-task",
    help="Add an editing task"
)

task_parser.add_argument(
    "--title",
    required=True
)

task_parser.add_argument(
    "--editor",
    required=True
)
#List Tak Commands
list_tasks_parser = subparsers.add_parser(
    "list-tasks",
    help="Display all tasks"
)

# COMPLETE TASK COMMAND

complete_task_parser = subparsers.add_parser(
    "complete-task",
    help="Mark a task as completed"
)

complete_task_parser.add_argument(
    "--title",
    required=True
)

# ASSIGN EDITOR COMMAND

assign_editor_parser = subparsers.add_parser(
    "assign-editor",
    help="Assign an editor to a book"
)

assign_editor_parser.add_argument(
    "--book",
    required=True
)

assign_editor_parser.add_argument(
    "--editor",
    required=True
)

# UPDATE MILESTONE COMMAND

milestone_parser = subparsers.add_parser(
    "update-milestone",
    help="Update a book milestone"
)

milestone_parser.add_argument(
    "--book",
    required=True
)

milestone_parser.add_argument(
    "--milestone",
    required=True
)

# Add Feedback Command

feedback_parser = subparsers.add_parser(
    "add-feedback",
    help="Add feedback to a task"
)

feedback_parser.add_argument(
    "--task",
    required=True
)

feedback_parser.add_argument(
    "--feedback",
    required=True
)

# VIEW FEEDBACK COMMAND

view_feedback_parser = subparsers.add_parser(
    "view-feedback",
    help="View task feedback"
)

view_feedback_parser.add_argument(
    "--task",
    required=True
)

# Read command line arguments
args = parser.parse_args()

# HANDLE COMMANDS

if args.command == "add-author":

    author = Author(
        args.name,
        args.email
    )

    data = load_data()

    data["authors"].append(
        {
            "id": author.id,
            "name": author.name,
            "email": author.email
        }
    )
    

    save_data(data)

    print(author)

elif args.command == "list-authors":

    data = load_data()

    for author in data["authors"]:
        print(
            f"ID: {author['id']} | "
            f"{author['name']} | "
            f"{author['email']}"
        )

elif args.command == "add-book":

    book = Book(
        args.title,
        args.genre,
        args.author
    )

    data = load_data()

    data["books"].append(
        {
            "id": book.id,
            "title": book.title,
            "genre": book.genre,
            "author": book.author,
            "editor": None,
            "milestone": book.milestone
        }
    )

    save_data(data)

    print(book)

elif args.command == "add-editor":

    editor = Editor(
        args.name,
        args.email
    )

    data = load_data()

    data["editors"].append(
        {
            "id": editor.id,
            "name": editor.name,
            "email": editor.email
        }
    )

    def __str__(self):
        return f"Editor ID: {self.id} | {self.name} | {self.email}"

    save_data(data)

    print(editor)

elif args.command == "list-editors":

    data = load_data()

    for editor in data["editors"]:
        print(
            f"ID: {editor['id']} | "
            f"{editor['name']} | "
            f"{editor['email']}"
        )

elif args.command == "list-books":

    data = load_data()

    for book in data["books"]:
        print(
            f"ID: {book['id']} | "
            f"{book['title']} | "
            f"{book['genre']} | "
            f"{book['milestone']}"
        )

elif args.command == "add-task":

    data = load_data()

    task = {
        "title": args.title,
        "editor": args.editor,
        "feedback": "",
        "status": "Pending"
    }

    data["tasks"].append(task)

    save_data(data)

    print(
        f"Task '{args.title}' assigned to {args.editor}"
    )

elif args.command == "list-tasks":

    data = load_data()

    for task in data["tasks"]:
        print(
            f"{task['title']} | "
            f"{task['editor']} | "
            f"{task['status']}"
        )

elif args.command == "complete-task":

    data = load_data()

    found = False

    for task in data["tasks"]:

        if task["title"] == args.title:

            task["status"] = "Completed"

            found = True

    save_data(data)

    if found:

        print(
            f"Task '{args.title}' completed."
        )

    else:

        print(
            "Task not found."
        )

elif args.command == "assign-editor":

    data = load_data()

    found = False

    for book in data["books"]:

        if book["title"] == args.book:

            book["editor"] = args.editor

            found = True

    save_data(data)

    if found:

        print(
            f"Editor '{args.editor}' assigned to '{args.book}'"
        )

    else:

        print(
            "Book not found."
        )

elif args.command == "update-milestone":

    valid_milestones = [
        "Draft",
        "Editing",
        "Review",
        "Published"
    ]

    if args.milestone not in valid_milestones:

        print(
            "Invalid milestone. Use:"
        )

        for milestone in valid_milestones:
            print(f"- {milestone}")

    else:

        data = load_data()

        found = False

        for book in data["books"]:

            if book["title"] == args.book:

                book["milestone"] = args.milestone

                found = True

        save_data(data)

        if found:

            print(
                f"Book '{args.book}' updated to "
                f"'{args.milestone}'"
            )

        else:

            print(
                "Book not found."
            )
elif args.command == "add-feedback":

    data = load_data()

    found = False

    for task in data["tasks"]:

        if task["title"] == args.task:

            task["feedback"] = args.feedback

            found = True

    save_data(data)

    if found:

        print("Feedback added.")

    else:

        print("Task not found.")

elif args.command == "view-feedback":

    data = load_data()

    found = False

    for task in data["tasks"]:

        if task["title"] == args.task:

            print(
                f"Feedback: "
                f"{task['feedback']}"
            )

            found = True

    if not found:

        print(
            "Task not found."
        )
