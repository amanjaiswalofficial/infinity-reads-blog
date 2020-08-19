import datetime
from typing import Tuple, List
from mongoengine import DoesNotExist, ValidationError,\
    InvalidQueryError

from .models import Blog, blog_schema, blogs_schema


def _get_blog_obj(id: str) -> Blog:
    """
    function to get a particular blog object or
    return error if it doesn't exist.
    :param id: id of a blog.
    :return: blog object or doesn't exist error.
    """
    try:
        blog = Blog.objects.get(pk=id)
    except (DoesNotExist, ValidationError) as error:
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

    if not error:
        obj = [blog_schema.dump(obj)]
    return obj, error


def get_blogs(search: str = None, sort_by: str = None,
              start: int = 0, limit: int = 20,) -> List:
    """
    function used to fetch all the blogs
    :param search:
    :param sort_by:
    :param start:
    :param limit:
    :return: List of blogs object
    """

    order_by = tuple(sort_by.split(",")) if sort_by else ("-created_at",)

    if search:
        blogs = Blog.objects(title__icontains=search).order_by(*order_by)
    else:
        blogs = Blog.objects().order_by(*order_by)

    # extract result according to bounds

    return blogs_schema.dump(blogs[start:limit + start])


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
    obj, error = _get_blog_obj(id)

    if error:
        return None, error

    payload["updated_at"] = datetime.datetime.now()
    try:
        obj.update(**payload)
        blog, error = get_blog(id=id)
        return blog, error
    except (InvalidQueryError, ValidationError) as error:
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
