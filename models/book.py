# This module defines the Book class, which represents a book in the book publishing workflow manager. The Book class includes attributes such as title, genre, author, editor, tasks, and milestone, as well as a unique ID for each book.
class Book:

    id_counter = 1 # Class variable to keep track of the next available ID for books.
    
    # Initializes a Book object with a title, genre, and author. It assigns a unique ID to the book and initializes the editor, tasks, and milestone attributes.
    def __init__(self, title, genre, author):
        self.id = Book.id_counter
        Book.id_counter += 1

        # Initializes the title, genre, and author attributes of the Book object.
        self.title = title
        self.genre = genre
        self.author = author

        self.editor = None

        self.tasks = []

        self.milestone = "Draft"
    # String representation of the Book object.


    def __str__(self):
        return (
            f"Book ID: {self.id} | "
            f"Title: {self.title} | "
            f"Milestone: {self.milestone}"
    )