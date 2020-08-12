from app.blog.constants import BlogMessage
from app.utils.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from tests.unittests.constants import PAYLOAD, PAYLOAD_WRONG, FIELD_REQUIRED, \
    DOES_NOT_EXIST, PAYLOAD_UPDATE, STRING_VALIDATION_ERROR, BULK_BLOGS


class TestBlogView:
    """
    This class used to test blog views.py
    """
    def test_create_blog_ok(self, test_client, init_blog, module_mocker):
        """
        success case to create a particular blog.
        :param test_client:
        :param init_blog:
        :param module_mocker:
        :return:
        """
        module_mocker.patch('app.blog.views.create_blog',
                            return_value=(init_blog, None))

        response = test_client.post('/blog',
                                    json=PAYLOAD)

        assert response.status_code == HTTP_200_OK
        assert response.json.get('code') == HTTP_200_OK
        assert response.json.get('errors') is None

    def test_create_blog_fail(self, test_client, module_mocker):
        """
        failure case of create blog if request payload is wrong.
        :param test_client:
        :return:
        """
        module_mocker.patch('app.blog.views.create_blog',
                            return_value=(None, FIELD_REQUIRED))

        response = test_client.post('/blog',
                                    json=PAYLOAD_WRONG)

        assert response.status_code == HTTP_200_OK
        assert response.json.get('code') == HTTP_400_BAD_REQUEST
        assert response.json.get("message") == FIELD_REQUIRED

    def test_get_blog_ok(self, test_client, module_mocker):
        """
        success case to fetch a particular blog based upon id.
        :param test_client:
        :param module_mocker:
        :return:
        """
        module_mocker.patch('app.blog.views.get_blog',
                            return_value=([PAYLOAD], None))

        response = test_client.get('/blog/123456789')

        assert response.status_code == HTTP_200_OK
        assert response.json.get("data")[0] == PAYLOAD

    def test_get_blog_fail(self, test_client, module_mocker):
        """
        failure case to fetch a particular blog if the blog
        doesn't exists in db.
        :param test_client:
        :param module_mocker:
        :return:
        """
        module_mocker.patch('app.blog.views.get_blog',
                            return_value=(None, DOES_NOT_EXIST))

        response = test_client.get('/blog/123456789')

        assert response.json.get('code') == HTTP_400_BAD_REQUEST
        assert response.json.get("message") == DOES_NOT_EXIST

    def test_update_blog_ok(self, test_client, module_mocker):
        """
        success case to update a blog.
        :param test_client:
        :param module_mocker:
        :return:
        """
        module_mocker.patch('app.blog.views.update_blog',
                            return_value=(None, None))

        response = test_client.put('/blog/123456789',
                                   json=PAYLOAD_UPDATE)

        assert response.json.get('code') == HTTP_200_OK
        assert response.json.get("message") == BlogMessage.UPDATE_SUCCESS

    def test_update_blog_fail(self, test_client, module_mocker):
        """
        failure case to update a blog having a wrong payload
        :param test_client:
        :param module_mocker:
        :return:
        """
        module_mocker.patch('app.blog.views.update_blog',
                            return_value=(None, STRING_VALIDATION_ERROR))

        response = test_client.put('/blog/123456789',
                                   json=PAYLOAD_WRONG)

        assert response.json.get('code') == HTTP_400_BAD_REQUEST
        assert response.json.get("message") == STRING_VALIDATION_ERROR

    def test_delete_blog_ok(self, test_client, module_mocker):
        """
        success case to delete a blog.
        :param test_client:
        :param module_mocker:
        :return:
        """
        module_mocker.patch('app.blog.views.delete_blog',
                            return_value=(None, None))

        response = test_client.delete('/blog/123412')

        assert response.json.get('code') == HTTP_200_OK
        assert response.json.get("message") == BlogMessage.DELETE_SUCCESS

    def test_delete_blog_fail(self, test_client, module_mocker):
        """
        failure case to delete a blog having blog doesn't exist.
        :param test_client:
        :param module_mocker:
        :return:
        """
        module_mocker.patch('app.blog.views.delete_blog',
                            return_value=(None, DOES_NOT_EXIST))

        response = test_client.delete('/blog/123412')

        assert response.json.get('code') == HTTP_400_BAD_REQUEST
        assert response.json.get("message") == DOES_NOT_EXIST

    def test_get_blogs_ok(self, test_client, module_mocker):
        """
        success case to fetch blogs.
        :param test_client:
        :param module_mocker:
        :return:
        """
        module_mocker.patch('app.blog.views.get_blogs',
                            return_value=BULK_BLOGS)

        response = test_client.get('/blogs')

        assert response.json.get('code') == HTTP_200_OK
        assert response.json.get("data") == BULK_BLOGS



