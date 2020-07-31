import datetime
from mongoengine import (Document, ReferenceField,
                         StringField, DateTimeField,
                         ListField, CASCADE)


class Blog(Document):
    user_id = StringField(max_length=20, required=True)
    title = StringField(max_length=120, required=True)
    content = StringField(required=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
    tags = ListField(StringField(max_length=30))

    def to_json(self):
        return {
            "_id": str(self.pk),
            "user_id": self.user_id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "tags": self.tags,
        }

    def comments(self):
        return Comment.objects(blog=self).all()


class Comment(Document):
    user_id = StringField(max_length=20, required=True)
    blog = ReferenceField(Blog, required=True, reverse_delete_rule=CASCADE)
    content = StringField(required=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)


class Like(Document):
    user_id = StringField(required=True)
    blog = ReferenceField(Blog, required=True, reverse_delete_rule=CASCADE)
    created_at = DateTimeField(default=datetime.datetime.now)
