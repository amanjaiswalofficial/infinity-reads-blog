from app.blog.models import blog_schema
from tests.unittests.constants import PAYLOAD, DOES_NOT_EXIST, PAYLOAD_UPDATE, PAYLOAD_WRONG, \
    STRING_VALIDATION_ERROR, PAYLOAD_WRONG1, FIELD_REQUIRED
from app.blog.service import _get_blog_obj, get_blogs, update_blog, \
    create_blog, get_blog


class TestBlogService:
    """
    Class to test blog services.py
    """
    def test_get_blog_obj_ok(self, init_blog):
        """
        GIVEN a blog
        WHEN _get_blog_obj() in blog service
        is called
        THEN get a particular blog object
        :param init_blog:
        :return: None
        """
        obj, error = _get_blog_obj(str(init_blog.id))
        assert str(obj.id) == str(init_blog.id)
        assert error is None

    def test_get_blog_obj_fail(self):
        """
        GIVEN a fake_id
        WHEN _get_blog_obj() in blog service
        is called
        THEN throws an error
        :return: None
        """
        obj, error = _get_blog_obj("fake_id")
        assert "fake_id" in str(error)
        assert obj is None

    def test_get_blog_obj_fail1(self):
        """
        GIVEN a wrong_id
        WHEN _get_blog_obj() in blog service
        is called
        THEN throws an error
        :return: None
        """
        obj, error = _get_blog_obj("5f31246634b63b01feed1745")
        assert DOES_NOT_EXIST in str(error)
        assert obj is None

    def test_get_blog_ok(self, init_blog):
        """
        GIVEN a blog
        WHEN get_blog() in blog service
        is called
        THEN get a particular blog
        :param init_blog:
        :return: None
        """
        result, error = get_blog(str(init_blog.id))
        assert result[0]['id'] == str(init_blog.id)
        assert result[0]['content'] == init_blog.content
        assert error is None

    def test_get_blog_ok_fail(self):
        """
        GIVEN a wrong_id
        WHEN get_blog() in blog service
        is called
        THEN throws an error that object
        doesn't exists.
        :return: None
        """
        result, error = get_blog("5f31246634b63b01feed1745")
        assert DOES_NOT_EXIST in str(error)
        assert result is None

    def test_get_blogs_ok(self):
        """
        GIVEN a wrong_id
        WHEN get_blog() in blog service
        is called
        THEN throws an error that object
        doesn't exists.
        :return: None
        """
        result = get_blogs(0, 1)
        assert len(result) == 1
        assert type(result) is list

    def test_update_blog_ok(self, init_blog):
        """
        GIVEN a blog
        WHEN update_blog() in blog service
        is called
        THEN get a particular blog object
        is updated
        :param init_blog:
        :return: None
        """
        result, error = update_blog(str(init_blog.id), PAYLOAD_UPDATE)
        assert result[0]['title'] == PAYLOAD_UPDATE['title']
        assert error is None

    def test_update_blog_fail(self, init_blog):
        """
        GIVEN a blog
        WHEN update_blog() in blog service
        is called
        THEN it throws an error
        :param init_blog:
        :return: None
        """
        result, error = update_blog(str(init_blog.id), PAYLOAD_WRONG1)
        assert result is None
        assert STRING_VALIDATION_ERROR in str(error)

    def test_create_blog_ok(self):
        """
        GIVEN a blog
        WHEN create_blog() in blog service
        is called
        THEN get a particular blog object
        is created
        :return: None
        """
        obj, error = create_blog(PAYLOAD)
        assert blog_schema.dump(obj)['title'] == PAYLOAD['title']
        assert blog_schema.dump(obj)['content'] == PAYLOAD['content']
        assert error is None

    def test_create_blog_fail(self):
        """
        GIVEN a blog
        WHEN create_blog() in blog service
        is called
        THEN it throw an error
        :return: None
        """
        result, error = create_blog(PAYLOAD_WRONG)
        assert FIELD_REQUIRED in str(error)
        assert result is None
