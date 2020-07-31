from .models import Blog

import datetime
from mongoengine import DoesNotExist, ValidationError, InvalidQueryError


def get_blog_obj(id: str):
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
    return blog, None


def get_blog(id: str):
    """
    Function used to fetch particular blog or
    return error if it is doesn't exist.
    :param id:
    :return:
    """
    obj, error = get_blog_obj(id)
    return obj.to_json(), error


def create_blog(payload: dict):
    """
    function used to create a particular blog.
    :param payload: details of blog in dict format.
    :return: blog object or Any validation error.
    """
    try:
        obj = Blog(**payload).save()
    except ValidationError as error:
        return None, error
    return obj, None


def update_blog(id: str, payload: dict):
    """
    function used to update a particular blog.
    :param id: id of blog.
    :param payload: details of blog in dict format.
    :return: blog object or Any validation or InvalidQuery error.
    """
    try:
        obj, error = get_blog_obj(id)
        if obj:
            payload["updated_at"] = datetime.datetime.now()
            obj.update(**payload)
            return "Blog object updated successfully", None
        return None, error
    except InvalidQueryError as error:
        return None, error
    except ValidationError as error:
        return None, error


def delete_blog(id: str):
    """
    Function used to delete a particular blog
    :param id:
    :return:
    """
    obj, error = get_blog_obj(id)
    if obj:
        obj.delete()
        return "Blog object deleted successfully", None
    return None, error
