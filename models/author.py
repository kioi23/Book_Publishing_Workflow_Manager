# This module defines the Author class, which inherits from the Person class and represents an author in the book publishing workflow manager.
from models.person import Person

# The Author class represents an author in the book publishing workflow manager. It inherits from the Person class and includes additional attributes and methods specific to authors.
class Author(Person):

    id_counter = 1

# Initializes an Author object with a name and email, and assigns a unique ID to the author. It also initializes an empty list of books associated with the author.
    def __init__(self, name, email):
        super().__init__(name, email)

        self.id = Author.id_counter
        Author.id_counter += 1
        # Initializes an empty list of books associated with the author.
        self.books = []