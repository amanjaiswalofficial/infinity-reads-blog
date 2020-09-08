from flask import Flask
from app.db import MongoAlchemy
from flask_marshmallow import Marshmallow
from app.seed import init_seed_script
from app.rabbitmq import RabbitMQ, Queue

# Globally accessible libraries
db = MongoAlchemy()
ma = Marshmallow()
rbmq = RabbitMQ()
queue = Queue()


def create_app(**kwargs):
    """Initialize the core application."""
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    db.init_app(app)
    ma.init_app(app)
    rbmq.init_app(app, queue)

    with app.app_context():
        from app.blog.views import blog
        # Register blueprint(s)
        app.register_blueprint(blog)

        init_seed_script()
        return app


# Need to import all the callbacks and queues
# that we define as it is required by queue object
from app.rabbitmq import callbacks
