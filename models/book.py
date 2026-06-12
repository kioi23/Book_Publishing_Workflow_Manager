class Book:

    id_counter = 1

    def __init__(self, title, genre, author):
        self.id = Book.id_counter
        Book.id_counter += 1

        self.title = title
        self.genre = genre
        self.author = author

        self.editor = None
        self.tasks = []
        self.milestone = "Draft"

    def __str__(self):
        return (
            f"Book ID: {self.id} | "
            f"Title: {self.title} | "
            f"Milestone: {self.milestone}"
        )