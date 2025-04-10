class Note:
    """A class to represent a note with title and content.

    Attributes:
        title (str): The title of the note
        content (str): The content of the note
    """

    def __init__(self, title, content):
        """Initialize a Note object.

        Args:
            title (str): The title of the note
            content (str): The content of the note
        """
        self.title = title
        self.content = content

    @property
    def title(self):
        """Get the title of the note."""
        return self._title

    @title.setter
    def title(self, value):
        """Set the title of the note."""
        self._title = value

    @property
    def content(self):
        """Get the content of the note."""
        return self._content

    @content.setter
    def content(self, value):
        """Set the content of the note."""
        self._content = value

    @classmethod
    def parse_from_json(cls, json_data):
        """Parse note data from a JSON dictionary.

        Args:
            json_data (dict): Dictionary containing title and content

        Returns:
            Note: A new Note instance created from the JSON data
        """
        return cls(json_data['title'], json_data['content'])

    def to_json(self):
        """Convert note to a JSON serializable dictionary.

        Returns:
            dict: Dictionary with title and content
        """
        return {
            'title': self.title,
            'content': self.content
        }
