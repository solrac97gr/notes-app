from flask import Blueprint, jsonify, request
from notes.domain.entities.notes import Note
from typing import Protocol, Any, List
from notes.application.services import NoteService
from shared.ports.logger_abs import LoggerAbs


class NotesController:
    def __init__(self, logger:LoggerAbs, service: NoteService):
        self.logger = logger
        self.service = service
        self.notes_bp = Blueprint('notes', __name__, url_prefix='/notes')

        # Initialize routes
        self.notes_bp.route('/', methods=['GET'])(self.router)
        self.notes_bp.route('/', methods=['POST'])(self.create)
        self.notes_bp.route('/<string:id>', methods=['GET'])(self.get)
        self.notes_bp.route('/<string:id>', methods=['PUT'])(self.update)
        self.notes_bp.route('/<string:id>', methods=['DELETE'])(self.delete)

    def get_blueprint(self):
        return self.notes_bp

    def router(self):
        self.logger.info("Getting all notes")
        notes = self.service.get_all_notes()
        return jsonify([note.to_json() for note in notes]), 200

    def create(self):
        self.logger.info("Creating a new note")
        data = request.get_json()
        note = self.service.create_note(data)
        return jsonify(note.to_json()), 201

    def get(self, id: str):
        self.logger.info(f"Getting note with id: {id}")
        try:
            note = self.service.get_note_by_id(id)
            return jsonify(note.to_json()), 200
        except IndexError:
            self.logger.error(f"Note with id {id} not found")
            return jsonify({'error': 'Note not found'}), 404

    def update(self, id: str):
        self.logger.info(f"Updating note with id: {id}")
        data = request.get_json()
        try:
            self.service.update_note(id, data)
            return jsonify({'message': 'Note updated'}), 200
        except IndexError:
            self.logger.error(f"Note with id {id} not found")
            return jsonify({'error': 'Note not found'}), 404

    def delete(self, id: str):
        self.logger.info(f"Deleting note with id: {id}")
        try:
            self.service.delete_note_by_id(id)
            return jsonify({'message': 'Note deleted'}), 200
        except IndexError:
            self.logger.error(f"Note with id {id} not found")
            return jsonify({'error': 'Note not found'}), 404
