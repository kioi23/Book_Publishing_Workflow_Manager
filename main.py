# This is the main entry point for the Book Publishing Workflow Manager CLI tool. It sets up the command-line interface, handles user input, and coordinates interactions between the various components of the application, such as models and utilities.
import argparse 
# The argparse module is used to create a command-line interface for the Book Publishing Workflow Manager. It allows the user to specify commands and options when running the application from the terminal. 

from models.book import Book
from models.author import Author
from models.editor import Editor
from models.task import Task
from utils.storage import save_data, load_data 


parser = argparse.ArgumentParser(
    description="Book Publishing Workflow Manager"
) # Creates an ArgumentParser object with a description of the application. This object will be used to define the command-line arguments and options for the application.

