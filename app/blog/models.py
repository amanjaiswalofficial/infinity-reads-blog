from app import ma

import datetime
from bson import ObjectId
from marshmallow import Schema, fields
from mongoengine import (Document, ReferenceField,
                         StringField, DateTimeField,
                         ListField, CASCADE)


Schema.TYPE_MAPPING[ObjectId] = fields.String


class Base(Document):
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    meta = {'abstract': True}


class Blog(Base):
    user_id = StringField(max_length=20, required=True)
    title = StringField(max_length=120, required=True)
    content = StringField(required=True)
    tags = ListField(StringField(max_length=30))

    def __repr__(self):
        return "<Blog %r>" % self.title

    def comments(self):
        return Comment.objects(blog=self).all()


class Comment(Base):
    user_id = StringField(max_length=20, required=True)
    blog = ReferenceField(Blog, required=True, reverse_delete_rule=CASCADE)
    content = StringField(required=True)


class Like(Document):
    user_id = StringField(required=True)
    blog = ReferenceField(Blog, required=True, reverse_delete_rule=CASCADE)
    created_at = DateTimeField(default=datetime.datetime.now)


class BlogSchema(ma.Schema):
    """
    Defined Blog Schema
    """

    class Meta:
        model = Blog
        fields = ('id', 'user_id', 'title', 'content', 'created_at', 'updated_at', 'tags')


blog_schema = BlogSchema()
blogs_schema = BlogSchema(many=True)
