from flask import Blueprint
from notes.infrastructure.store.mongo import MongoRepository
from notes.application.services import NoteService
from notes.infrastructure.http.controller import NotesController
from shared.ports.logger_abs import LoggerAbs


def register_notes_app(router: Blueprint, logger: LoggerAbs):
    mongo_repository = MongoRepository("mongodb://localhost:27017", "flask_app", "notes", logger)
    note_service = NoteService(mongo_repository, logger)
    notes_controller = NotesController(logger, note_service)
    
    # Register the routes directly on the v1 blueprint
    # This way all routes will be properly prefixed with /v1/notes
    router.register_blueprint(notes_controller.get_blueprint())
