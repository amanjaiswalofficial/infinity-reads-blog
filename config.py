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

# ######################## #
# #### Configurations #### #
# ######################## #


DEBUG = env('DEBUG')
