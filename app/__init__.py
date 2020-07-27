from flask import Flask


def create_app(**kwargs):
    """Initialize the core application."""
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    with app.app_context():
        return app