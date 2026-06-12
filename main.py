import argparse

from models.author import Author
from models.book import Book
from models.editor import Editor
from utils.storage import load_data, save_data

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

    save_data(data)

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