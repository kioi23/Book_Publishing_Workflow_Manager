# This module defines the Editor class, which inherits from the Person class and represents an editor in the book publishing workflow manager.
from models.person import Person

# The Editor class represents an editor in the book publishing workflow manager. It inherits from the Person class and includes additional attributes and methods specific to editors.
class Editor(Person):

    id_counter = 1

    # Initializes an Editor object with a name and email, and assigns a unique ID to the editor. It also initializes an empty list of books assigned to the editor.
    def __init__(self, name, email):
        super().__init__(name, email)

        self.id = Editor.id_counter
        Editor.id_counter += 1

        self.assigned_books = []