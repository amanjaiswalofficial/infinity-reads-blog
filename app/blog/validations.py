from typing import List, Union

from flask import request

from app.blog.models import blog_schema


def _get_error_list(_errors: dict) -> Union[List, None]:
    """
    This method return a list of errors,
    if any exists
    :param _errors: Dict of errors
    :return: List of errors or None
    """
    errors = []
    for err in _errors:
        errors.append({
            "field": err,
            "msg": _errors.get(err, "")
        })
    return errors if errors else None


def blog_validate() -> Union[List, None]:
    """
    This method validates the data
    during creating blog and returns the
    list of errors, if any exists.
    :return: List of errors or None
    """
    payload = request.get_json()
    errors = blog_schema.validate(payload)
    return errors  # currently passing the direct error without using _get_error_list

