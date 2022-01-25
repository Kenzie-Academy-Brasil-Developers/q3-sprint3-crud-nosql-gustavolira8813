
from datetime import datetime

class Post:
    def __init__(self, id, title, author, tags, content) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content
        self.created_at = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")
        self.updated_at = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")