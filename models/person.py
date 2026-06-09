# This module defines the Person class, which serves as a base class for Author and Editor.

class Person:
    
     # Base class for Author and Editor.
    
    # Initializes a Person object with a name and email.
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # String representation of the Person object.
    def __str__(self):
        return f"{self.name} ({self.email})" # String representation of the Person object.