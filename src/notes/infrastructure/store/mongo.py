from pymongo import MongoClient
from notes.domain.ports.repository import RepositoryPort
from notes.domain.entities.notes import Note
from shared.ports.logger_abs import LoggerAbs

class MongoRepository(RepositoryPort):
    def __init__(self, uri: str, db_name: str, collection_name: str, logger: LoggerAbs):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        self.logger = logger

    def save(self, note: Note) -> None:
        self.logger.info(f"Saving note with id {note.id}")
        self.collection.insert_one(note.to_json())

    def find_by_id(self, id: str) -> Note:
        self.logger.info(f"Finding note with id {id}")
        result = self.collection.find_one({"id": id})
        if result is None:
            self.logger.error(f"Note with id {id} not found")
            raise ValueError(f"Note with id {id} not found")
        return Note(**result)

    def find_all(self) -> list[Note]:
        self.logger.info(f"Finding all notes")
        results = list(self.collection.find({}))
        self.logger.info(f"Found {len(results)} notes")
        return [Note(**result) for result in results]

    def delete(self, id: str) -> None:
        self.logger.info(f"Deleting note with id {id}")
        self.collection.delete_one({"id": id})

    def update(self, id: str, note: dict) -> None:
        self.logger.info(f"Updating note with id {id}")
        self.collection.update_one({"id": id}, {"$set": note})
