from models.person import Person

class Author(Person):
    """
    Represents an author in the publishing system.
    """

    id_counter = 1

    def __init__(self, name, email):
        super().__init__(name, email)

        self.id = Author.id_counter
        Author.id_counter += 1

        self.books = []

    def __str__(self): 
        return f"Author ID: {self.id} | {self.name} | {self.email}"