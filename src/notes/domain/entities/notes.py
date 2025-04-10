class Note:
    """A class to represent a note with title and content.

    Attributes:
        id (str): The unique identifier of the note
        title (str): The title of the note
        content (str): The content of the note
    """

    def __init__(self, title, content, id=None):
        """Initialize a Note object.

        Args:
            title (str): The title of the note
            content (str): The content of the note
            id (str, optional): The unique identifier of the note. Defaults to None.
        """
        self.title = title
        self.content = content
        self.id = id

    @property
    def id(self):
        """Get the id of the note."""
        return self._id

    @id.setter
    def id(self, value):
        """Set the id of the note."""
        self._id = value

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
            json_data (dict): Dictionary containing title, content, and optionally id

        Returns:
            Note: A new Note instance created from the JSON data
        """
        return cls(json_data['title'], json_data['content'], json_data.get('id'))

    def to_json(self):
        """Convert note to a JSON serializable dictionary.

        Returns:
            dict: Dictionary with id, title and content
        """
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content
        }
