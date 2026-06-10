class Task:
    """
    Represents an editing task.
    """

    def __init__(self, title, editor):
        self.title = title
        self.editor = editor
        self.feedback = ""
        self.status = "Pending"

    def complete_task(self):
        self.status = "Completed"

    def __str__(self):
        return f"{self.title} - {self.status}"
    