from abc import ABC, abstractmethod
from notes.domain.entities.notes import Note

class NoteServicePort(ABC):
    @abstractmethod
    def create_note(self, note_data: dict) -> Note:
        pass

    @abstractmethod
    def get_note_by_id(self, note_id: str) -> Note:
        pass

    @abstractmethod
    def get_all_notes(self) -> list:
        pass

    @abstractmethod
    def update_note(self, note_id: str, updated_data: dict) -> None:
        pass

    @abstractmethod
    def delete_note_by_id(self, note_id: str) -> None:
        pass
