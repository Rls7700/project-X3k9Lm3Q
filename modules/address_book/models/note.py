from datetime import datetime
from .common import Field
import uuid

class Note(Field):
    def __init__(self, value):
        self.id = uuid.uuid4().hex[:12]
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.tags = []
        super().__init__(value)

    def change(self, value):
        self.updated_at = datetime.now()
        self.value = value

    def add_tag(self, tag: str):
        if not tag.startswith('#'):
            tag = f"#{tag}"
            
        if tag not in self.tags:
            self.tags.append(tag)
            self.updated_at = datetime.now()

    def __str__(self):
        tags_str = f"Tags: {', '.join(self.tags)}\n" if self.tags else ""
        return (
            f"ID: {self.id}\n"
            f"Created: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Updated: {self.updated_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"{tags_str}"
            f"Note: {self.value}\n\n"
        )
    