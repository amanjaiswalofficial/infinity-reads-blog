from flask import Flask
from app.db import MongoAlchemy

# Globally accessible libraries
ma = MongoAlchemy()


def create_app(**kwargs):
    """Initialize the core application."""
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    ma.init_app(app)

    with app.app_context():
        from app.blog.views import blog
        app.register_blueprint(blog)

        return app
