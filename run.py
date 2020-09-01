from flask import Flask

from app import create_app
from app import rbmq

app = Flask(__name__)


if __name__ == "__main__":
    app = create_app()
    rbmq.run()  # to start rabbitmq consumer
    app.run(debug=True)
