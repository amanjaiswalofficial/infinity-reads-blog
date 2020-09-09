"""This file contains code to run seed script"""
import json
import os

from flask import current_app
from app.blog.models import Blog
from app.logger import logger
from app.utils.constants import SeedMessage


def init_product() -> None:
    """
    This function will initialize the database for Blogs using MongoDB
    :return: None
    """
    blogs_to_insert = []
    blog_table_name = Blog._get_collection().name

    # get data from seed file for blogs
    item_seed_path = \
        os.path.join(current_app.root_path, "blog", "seed.json")
    with open(item_seed_path) as seed_data:
        blog_seed_data = json.load(seed_data)
        blogs = blog_seed_data.get(blog_table_name)

    blog_count = Blog.objects.count()
    # if seed_script is not running for the first time
    if blog_count:
        logger.info(SeedMessage.DATA_ALREADY_EXISTS.format(blog_table_name))
    else:
        # if seed script is running for the first time, insert records
        for blog in blogs:
            blog_instance = Blog(**blog)
            blogs_to_insert.append(blog_instance)

        # Bulk Insert Records
        Blog.objects.insert(blogs_to_insert)

        logger.info(SeedMessage.WRITING_SUCCESSFUL.format(blog_table_name))


def execute() -> None:
    """
    Executor for seed script for db
    :return: None
    """
    init_product()
