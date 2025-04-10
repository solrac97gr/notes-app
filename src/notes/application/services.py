from notes.domain.entities.notes import Note
from notes.domain.ports.service import NoteServicePort
from notes.domain.ports.repository import RepositoryPort
from shared.ports.logger_abs import LoggerAbs

class NoteService(NoteServicePort):
    def __init__(self, repository: RepositoryPort, logger: LoggerAbs):
        self.repository = repository
        self.logger = logger

    def create_note(self, note_data: dict) -> Note:
        note = Note.parse_from_json(note_data)
        self.repository.save(note)
        self.logger.info(f"Note with ID {note.id} created successfully.")
        return note

    def get_note_by_id(self, note_id: str) -> Note:
        note = self.repository.find_by_id(note_id)
        if not note:
            self.logger.error(f"Note with ID {note_id} not found.")
            raise ValueError("Note not found")

        return note

    def get_all_notes(self) -> list[Note]:
        notes = self.repository.find_all()
        self.logger.info(f"Retrieved {len(notes)} notes.")
        return notes

    def update_note(self, note_id: str, updated_data: dict) -> None:
        self.repository.update(note_id, updated_data)

    def delete_note_by_id(self, note_id: str) -> None:
        self.repository.delete(note_id)
        self.logger.info(f"Note with ID {note_id} deleted successfully.")
