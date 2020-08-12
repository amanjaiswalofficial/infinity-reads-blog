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
        success case to get a particular blog
        :param init_blog:
        :return:
        """
        obj, error = _get_blog_obj(str(init_blog.id))
        assert str(obj.id) == str(init_blog.id)
        assert error is None

    def test_get_blog_obj_fail(self):
        """
        failure case to get a particular blog with wrong id
        :return:
        """
        obj, error = _get_blog_obj("fake_id")
        assert "fake_id" in str(error)
        assert obj is None

    def test_get_blog_obj_fail1(self):
        """
        failure case to get a particular blog with wrong id
        :return:
        """
        obj, error = _get_blog_obj("5f31246634b63b01feed1745")
        assert DOES_NOT_EXIST in str(error)
        assert obj is None

    def test_get_blog_ok(self, init_blog):
        """
        success case to get a particular blog.
        :param init_blog:
        :return:
        """
        result, error = get_blog(str(init_blog.id))
        assert result[0]['_id'] == str(init_blog.id)
        assert result[0]['content'] == init_blog.content
        assert error is None

    def test_get_blog_ok_fail(self):
        """
        failure case to get a particular blog with wrong id
        :return:
        """
        result, error = get_blog("5f31246634b63b01feed1745")
        assert DOES_NOT_EXIST in str(error)
        assert result is None

    def test_get_blogs_ok(self):
        """
        success case to get a particular blogs.
        :return:
        """
        result = get_blogs(0, 1)
        assert len(result) == 1
        assert type(result) is list

    def test_update_blog_ok(self, init_blog):
        """
        success case to get a update a blog.
        :param init_blog:
        :return:
        """
        result, error = update_blog(str(init_blog.id), PAYLOAD_UPDATE)
        assert result is None
        assert error is None

    def test_update_blog_fail(self, init_blog):
        """
        failure case to update a particular blog with wrong
        payload.
        :param init_blog:
        :return:
        """
        result, error = update_blog(str(init_blog.id), PAYLOAD_WRONG1)
        assert result is None
        assert STRING_VALIDATION_ERROR in str(error)

    def test_create_blog_ok(self):
        """
        success case to create a particular blog.
        :return:
        """
        obj, error = create_blog(PAYLOAD)
        assert obj.to_json()['title'] == PAYLOAD['title']
        assert obj.to_json()['content'] == PAYLOAD['content']
        assert error is None

    def test_create_blog_fail(self):
        """
        failure case to create a particular blog with wrong
        payload.
        :return:
        """

        result, error = create_blog(PAYLOAD_WRONG)
        assert FIELD_REQUIRED in str(error)
        assert result is None
