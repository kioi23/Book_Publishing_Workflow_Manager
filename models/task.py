# This module defines the Book class, which represents a book in the book publishing workflow manager. The Book class includes attributes such as title, genre, author, editor, tasks, and milestone, as well as a unique ID for each book.
class Task:

    def __init__(self, title, editor): # Initializes a Task object with a title and an editor. It also initializes the feedback and status attributes of the task.
        self.title = title
        self.editor = editor

        self.feedback = ""

        self.status = "Pending"

# encapsuation of the Book class, which includes attributes and methods related to a book in the publishing workflow.

@property # Getter for the milestone attribute of the Book class. It returns the current milestone of the book.


def milestone(self):
    return self._milestone

@milestone.setter # Setter for the milestone attribute of the Book class. It validates the input value against a list of valid milestones and sets the milestone if the value is valid. If the value is invalid, it raises a ValueError.

# The setter for the milestone attribute of the Book class validates the input value against a list of valid milestones. If the value is not in the list of valid milestones, it raises a ValueError with the message "Invalid milestone". If the value is valid, it sets the _milestone attribute to the input value.
def milestone(self, value):

    valid = [
        "Draft",
        "Editing",
        "Review",
        "Published"
    ] # List of valid milestones for a book in the publishing workflow.

    # Validates the input value against a list of valid milestones. If the value is not in the list of valid milestones, it raises a ValueError with the message "Invalid milestone".
    if value not in valid:
        raise ValueError("Invalid milestone")

    self._milestone = value