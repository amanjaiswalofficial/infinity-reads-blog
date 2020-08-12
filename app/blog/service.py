import datetime
from typing import Tuple, List
from mongoengine import DoesNotExist, ValidationError,\
    InvalidQueryError

from .models import Blog


def _get_blog_obj(id: str) -> Blog:
    """
    function to get a particular blog object or
    return error if it doesn't exist.
    :param id: id of a blog.
    :return: blog object or doesn't exist error.
    """
    try:
        blog = Blog.objects.get(pk=id)
    except DoesNotExist as error:
        return None, error
    except ValidationError as error:
        return None, error
    return blog, None


def get_blog(id: str) -> Tuple:
    """
    Function used to fetch particular blog or
    return error if it is doesn't exist.
    :param id: blog id
    :return: tuple of (blog object or any error)
    """
    obj, error = _get_blog_obj(id)
    if obj:
        obj = [obj.to_json()]
    return obj, error


def get_blogs(start, limit) -> List:
    """
    function used to fetch all the blogs
    :return: List of blogs object
    """
    result = []
    start = int(start)
    limit = int(limit)

    # extract result according to bounds
    blogs = Blog.objects().order_by("-created_at")[start:limit+start]

    for blog in blogs:
        result.append(blog.to_json())

    return result


def create_blog(payload: dict) -> Tuple:
    """
    function used to create a particular blog.
    :param payload: details of blog in dict format.
    :return: Tuple of (blog object or Any validation error).
    """
    try:
        obj = Blog(**payload).save()
    except ValidationError as error:
        return None, error
    return obj, None


def update_blog(id: str, payload: dict) -> Tuple:
    """
    function used to update a particular blog.
    :param id: id of blog.
    :param payload: details of blog in dict format.
    :return: blog object or Any validation or InvalidQuery error.
    """
    try:
        obj, error = _get_blog_obj(id)
        if obj:
            payload["updated_at"] = datetime.datetime.now()
            obj.update(**payload)
            return None, None
        return None, error
    except InvalidQueryError as error:
        return None, error
    except ValidationError as error:
        return None, error


def delete_blog(id: str) -> Tuple:
    """
    Function used to delete a particular blog
    :param id:
    :return: tuple of (success message or any error)
    """
    obj, error = _get_blog_obj(id)
    if obj:
        obj.delete()
        return None, None
    return None, error
