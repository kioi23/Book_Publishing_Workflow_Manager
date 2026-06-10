# This is the main entry point for the Book Publishing Workflow Manager CLI tool. It sets up the command-line interface, handles user input, and coordinates interactions between the various components of the application, such as models and utilities.
import argparse 
# The argparse module is used to create a command-line interface for the Book Publishing Workflow Manager. It allows the user to specify commands and options when running the application from the terminal. 

parser = argparse.ArgumentParser(
    description="Book Publishing Workflow Manager"
) # Creates an ArgumentParser object with a description of the application. This object will be used to define the command-line arguments and options for the application.

subparsers = parser.add_subparsers(dest="command")

# add-author command
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
    print(
        f"Author Created: {args.name} ({args.email})"
    )


