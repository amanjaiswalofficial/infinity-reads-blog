from typing import Dict
from flask import Blueprint, request

from app.utils.response_helper import (success_response as success,
                                       failure_response as failure)
from app.blog.constants import BlogMessage
from .service import get_blog, create_blog, update_blog, \
    delete_blog, get_blogs

blog = Blueprint('blog', __name__)


@blog.route("/blog/<id>", methods=["GET", "PUT", "DELETE"])
def blog_view(id: str) -> Dict:
    """
    API to get, update and delete a particular blog.
    :return: success JSON response or failure message.
    """
    result = None
    error = None
    message = None

    if request.method == 'GET':
        result, error = get_blog(id)

    elif request.method == 'PUT':
        payload = request.get_json()
        result, error = update_blog(id, payload)
        message = BlogMessage.UPDATE_SUCCESS

    elif request.method == "DELETE":
        obj, error = delete_blog(id)
        message = BlogMessage.DELETE_SUCCESS
    return success(data=result, message=message) if not error else failure(message=error)


@blog.route("/blog", methods=["POST"])
def blog_create_view() -> Dict:
    """
    API to create a particular blog.
    :return: id of the created blog or any error message.
    """
    payload = request.get_json()
    obj, error = create_blog(payload)
    return success(data=[{"id": str(obj.id)}], message=BlogMessage.CREATE_SUCCESS)\
        if not error else failure(message=error)


@blog.route("/blogs/", methods=['GET'])
def blogs_view() -> Dict:
    """
    API to fetch all the blogs.
    :return: List of JSON response.
    """
    params = request.args
    start = int(params.get('start', 0))
    limit = int(params.get('limit', 20))
    search_by = params.get('search')
    sort_by = params.get('sort')
    result = get_blogs(search_by, sort_by,
                       start=start, limit=limit)
    return success(data=result)
