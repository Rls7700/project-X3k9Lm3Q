from datetime import datetime
from .common import Field
import uuid

class Note(Field):
    def __init__(self, value):
        self.id = uuid.uuid4().hex[:12]
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().__init__(value)

    def change(self, value):
        self.updated_at = datetime.now()
        self.value = value

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Created: {self.created_at}\n"
            f"Updated: {self.updated_at}\n"
            f"Note: {self.value}\n\n"
        )