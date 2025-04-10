from pymongo import MongoClient
from bson import ObjectId
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
        self.logger.info(f"Saving note with title {note.title}")
        note_dict = {
            'title': note.title,
            'content': note.content
        }
        result = self.collection.insert_one(note_dict)
        note.id = str(result.inserted_id)

    def find_by_id(self, id: str) -> Note:
        self.logger.info(f"Finding note with id {id}")
        try:
            object_id = ObjectId(id)
            result = self.collection.find_one({"_id": object_id})
            if result is None:
                self.logger.error(f"Note with id {id} not found")
                raise ValueError(f"Note with id {id} not found")
            note_id = str(result.pop('_id'))
            return Note(title=result['title'], content=result['content'], id=note_id)
        except Exception as e:
            self.logger.error(f"Error finding note: {str(e)}")
            raise ValueError(f"Note with id {id} not found")

    def find_all(self) -> list[Note]:
        self.logger.info(f"Finding all notes")
        results = list(self.collection.find({}))
        self.logger.info(f"Found {len(results)} notes")
        notes = []
        for result in results:
            note_id = str(result.pop('_id'))
            notes.append(Note(title=result['title'], content=result['content'], id=note_id))
        return notes

    def delete(self, id: str) -> None:
        self.logger.info(f"Deleting note with id {id}")
        try:
            object_id = ObjectId(id)
            self.collection.delete_one({"_id": object_id})
        except Exception as e:
            self.logger.error(f"Error deleting note: {str(e)}")
            raise ValueError(f"Note with id {id} not found")

    def update(self, id: str, note: dict) -> None:
        self.logger.info(f"Updating note with id {id}")
        try:
            object_id = ObjectId(id)
            if 'id' in note:
                del note['id']
            self.collection.update_one({"_id": object_id}, {"$set": note})
        except Exception as e:
            self.logger.error(f"Error updating note: {str(e)}")
            raise ValueError(f"Note with id {id} not found")
