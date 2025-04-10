from abc import ABC, abstractmethod
from notes.domain.entities.notes import Note


from notes.domain.entities.notes import Note

class RepositoryPort(ABC):
    @abstractmethod
    def save(self, note: Note) -> None:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> Note:
        pass

    @abstractmethod
    def find_all(self) -> list:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass

    @abstractmethod
    def update(self, id: str, note: dict) -> None:
        pass
