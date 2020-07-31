from flask import Blueprint, request

from .models import Blog
from app.utils.response_helper import (success_response as success,
                                       failure_response as failure)
from .service import get_blog, create_blog, update_blog, delete_blog

blog = Blueprint('blog', __name__)


@blog.route("/blog/<id>", methods=["GET", "PUT", "DELETE"])
def blog_view(id: str):
    """
    API to get, update and delete a particular blog.
    :return: success response or failure message.
    """
    error = None
    result = None

    if request.method == 'GET':
        result, error = get_blog(id)

    elif request.method == 'PUT':
        payload = request.get_json()
        result, error = update_blog(id, payload)
    else:
        obj, error = delete_blog(id)

    return success(data=result) if not error else failure(message=error)


@blog.route("/blog", methods=["POST"])
def blog_post_view():
    """
    API to create a particular blog.
    :return: id of the created blog or any error message.
    """
    payload = request.get_json()
    obj, error = create_blog(payload)
    return success(data={"id": str(obj.id)}) if not error else failure(message=error)


@blog.route("/blogs", methods=['GET'])
def blogs_view():
    """
    API to fetch all the blogs.
    :return: List of JSON response.
    """
    result = []
    blogs = Blog.objects
    for blog in blogs:
        result.append(blog.to_json())
    return success(data=result)
