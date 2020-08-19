"""Constant file for Utils"""


class SeedMessage(object):
    EXECUTE_MISSING = "Module named '{}' has no method execute"
    MODULE_MISSING = "Module named '{}' doesn't exist"
    WRITING_SEED_DATA = "Writing seed data for {}"
    WRITING_SUCCESSFUL = "Writing successful for {}"
    DATA_ALREADY_EXISTS = "Records for table: {} already exist, " \
                          "skipping writing seed data"


POOL_CHUNK_SIZE = 100
APP_NAME = "blog_app"
CONFIG_NOT_FOUND = "Config not found for {}, please check the config file."
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
CONNECTION_SUCCESSFUL = "Connection successful with: {}"
CONNECTION_REFUSED = "Unable to connect with the database. " \
                     "Ensure connection and credentials are correct."
