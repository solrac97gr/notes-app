# Flask Notes API

## Project Overview

This Flask Notes API is a learning project that demonstrates how to build a RESTful API using Flask with a clean architecture approach. The application allows users to create, read, update, and delete notes through well-defined API endpoints.

## Architecture

The project follows a hexagonal architecture (ports and adapters) pattern with clear separation of concerns:

- **Domain Layer**: Contains the core business logic and entities
- **Application Layer**: Implements use cases and orchestrates domain operations
- **Infrastructure Layer**: Handles external concerns like HTTP requests and database access
- **Shared Layer**: Cross-cutting concerns like logging

## Key Features

- RESTful API endpoints for note management
- MongoDB integration for data persistence
- Structured logging system
- Clean architecture implementation with dependency injection
- Blueprint-based route organization

## Project Structure

```
notes_app/src/
├── app.py                           # Main application entry point
├── notes/                           # Notes module
│   ├── __init__.py
│   ├── application/                 # Application layer
│   │   ├── __init__.py
│   │   └── services.py              # Service implementations
│   ├── domain/                      # Domain layer
│   │   ├── entities/                # Domain entities
│   │   │   ├── __init__.py
│   │   │   └── notes.py             # Note entity
│   │   └── ports/                   # Interfaces (ports)
│   │       ├── __init__.py
│   │       ├── repository.py        # Repository interface
│   │       └── service.py           # Service interface
│   ├── infrastructure/              # Infrastructure layer
│   │   ├── http/                    # HTTP concerns
│   │   │   ├── __init__.py
│   │   │   └── controller.py        # HTTP controllers
│   │   ├── store/                   # Data storage
│   │   │   ├── __init__.py
│   │   │   └── mongo.py             # MongoDB implementation
│   │   └── ui/                      # UI concerns
│   │       ├── __init__.py
│   │       └── templates.py         # UI templates
│   └── routes.py                    # Route definitions
└── shared/                          # Shared components
    ├── logger/                      # Logging module
    │   └── logger.py                # Logger implementation
    └── ports/                       # Shared interfaces
        └── logger_abs.py            # Logger abstract class
```

## Setup and Installation

### Prerequisites

- Python 3.8+
- MongoDB
- pip

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flask-notes-api.git
   cd flask-notes-api
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure MongoDB is running on localhost:27017 or update the connection string in `notes/routes.py`

5. Run the application:
   ```bash
   python src/app.py
   ```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v1/notes/` | GET | Get all notes |
| `/v1/notes/` | POST | Create a new note |
| `/v1/notes/{id}` | GET | Get a note by ID |
| `/v1/notes/{id}` | PUT | Update a note by ID |
| `/v1/notes/{id}` | DELETE | Delete a note by ID |

## Example API Usage

### Create a new note

```bash
curl -X POST http://localhost:5000/v1/notes/ \
  -H "Content-Type: application/json" \
  -d '{"title": "My First Note", "content": "This is a test note"}'
```

### Get all notes

```bash
curl http://localhost:5000/v1/notes/
```

## Learning Resources

This project was created as a learning exercise for Flask and clean architecture. Key concepts demonstrated:

- Hexagonal architecture in Python
- Dependency injection
- Interface-based programming
- RESTful API design
- MongoDB integration
- Flask blueprints
