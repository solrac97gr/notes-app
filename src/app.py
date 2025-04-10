from flask import Flask, Blueprint
from shared.logger.logger import Logger
from notes.routes import register_notes_app

# Initialize the logger
logger = Logger()

# Initialize the Flask app
app = Flask(__name__)

# Create a blueprint for version 1 of the API
v1 = Blueprint('v1', __name__, url_prefix='/v1')

# Register app with the blueprint and logger
register_notes_app(v1, logger)
#register_user_app(v1, logger)

# Register the blueprint with the Flask app
app.register_blueprint(v1)

if __name__ == '__main__':
    app.run(debug=True)
