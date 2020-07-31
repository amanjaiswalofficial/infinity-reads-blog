"""Main configuration file"""
# Define the application directory
from os import getenv, path
from environs import Env

BASE_DIR = path.abspath(path.dirname(__file__))
env = Env()

current_env = getenv('BLOG_ENV') or 'local'

if not path.exists("{}.env".format(current_env)):
    raise EnvironmentError("FLASK_ENV not set properly for {} env.".format(
        current_env))

# loading the selected .env file
project_folder = path.expanduser(BASE_DIR)
env.read_env(path.join(project_folder, "{}.env".format(current_env)))

# ######################## #
# #### Configurations #### #
# ######################## #


DEBUG = env('DEBUG')

# MongoDB Configuration
MONGODB_DATABASE_URI = env("MONGODB_DATABASE_URI")
MAX_POOL_SIZE = env.int("MAX_POOL_SIZE")
MIN_POOL_SIZE = env.int("MIN_POOL_SIZE")
MAX_IDLE_TIME = env.int("MAX_IDLE_TIME")
CONNECTION_TIMEOUT = env.int("CONNECTION_TIMEOUT")
HEARTBEAT_FREQUENCY = env.int("HEARTBEAT_FREQUENCY")
SERVER_SELECTION_TIMEOUT = env.int("SERVER_SELECTION_TIMEOUT")
