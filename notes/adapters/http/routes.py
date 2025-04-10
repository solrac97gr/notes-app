from flask import Blueprint, jsonify, request

from notes.domain.notes import Note

notes_bp = Blueprint('notes', __name__, url_prefix='/notes')

notes: list[Note] = []

notes.append(Note.parse_from_json({
    "title": "Primer nota",
    "content": "Contenido de la primera nota"
}))

notes.append(Note.parse_from_json({
    "title": "Segunda nota",
    "content": "Contenido de la segunda nota"
}))

@notes_bp.route('/', methods=['GET'])
def router():
    return jsonify([note.to_json() for note in notes]), 200

@notes_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    note = Note.parse_from_json(data)
    notes.append(note)
    return jsonify(note.to_json()), 201

@notes_bp.route('/<int:id>', methods=['GET'])
def get(id: int):
    note = notes[id]
    if note is None:
        return jsonify({'error': 'Note not found'}), 404
    return jsonify(note.to_json()), 200

@notes_bp.route('/<int:id>', methods=['PUT'])
def update(id: int):
    note = notes[id]
    if note is None:
        return jsonify({'error': 'Note not found'}), 404
    data = request.get_json()

    if 'title' in data:
        note.title = data['title']
    if 'content' in data:
        note.content = data['content']

    return jsonify(note.to_json()), 200

@notes_bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    note = notes[id]
    if note is None:
        return jsonify({'error': 'Note not found'}), 404
    notes.remove(note)
    return jsonify({'message': 'Note deleted'}), 200
