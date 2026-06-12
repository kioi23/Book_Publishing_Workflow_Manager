import argparse

from models.author import Author
from models.book import Book

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

# Read command line arguments
args = parser.parse_args()

# HANDLE COMMANDS

if args.command == "add-author":

    author = Author(
        args.name,
        args.email
    )

    print(author)

elif args.command == "add-book":

    book = Book(
        args.title,
        args.genre,
        args.author
    )

    print(book)