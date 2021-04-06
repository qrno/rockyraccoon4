import enum

class LineType(enum.Enum):
    Attribute = "ATTRIBUTE"
    Content   = "Content"

class Line:
    def __init__(self, type, content):
        self.type = type
        self.content = content
