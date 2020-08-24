# All fixtures will be added here.
# Make sure you add those fixtures
# which have usage all over the module.
import pytest


@pytest.fixture(scope='module')
def test_client():
    from app import create_app
    app = create_app()
    app.config['TESTING'] = True

    # Flask provides a way to test your application
    # by exposing the Werkzeug test Client and
    # handling the context locals for you.
    testing_client = app.test_client()

    # Establish an application context
    # before running the tests.
    ctx = app.app_context()
    ctx.push()

    yield testing_client  # This is where testing happens

    ctx.pop()


@pytest.fixture(scope='module')
def init_blog(test_client):
    """
    This method will create
    a dummy blog.
    :return: None
    """
    from app.blog.models import Blog

    try:
        payload = {
            "title": "title test",
            "content": "content test",
            "user_id": "234567890",
            "tags": ["dummy"]
        }

        obj = Blog(**payload).save()

        yield obj  # provide the fixture value

    except Exception as err:
        raise Exception(err)

    finally:
        # Teardown blog object
        obj.delete()
        print("object deleted successfully")

