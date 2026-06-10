import argparse

from models.author import Author

parser = argparse.ArgumentParser(
    description="Book Publishing Workflow Manager"
)

subparsers = parser.add_subparsers(dest="command")

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

args = parser.parse_args()

if args.command == "add-author":

    author = Author(
        args.name,
        args.email
    )

    print(author)
    