PAYLOAD = {
    "title": "title 1",
    "content": "content",
    "user_id": "234567890"
}

PAYLOAD_WRONG = {
    "content": "content",
    "user_id": "234567890"
}

PAYLOAD_WRONG1 = {
    "title": 123456789
}

PAYLOAD_UPDATE = {
    "title": "title updated"
}

BULK_BLOGS = {'blogs': [PAYLOAD, PAYLOAD], 'total_count': 2}

TAGS = {'tags': ['dummy', 'test_tag']}

FIELD_REQUIRED = "ValidationError (Blog:None) (Field is required: ['title'])"
DOES_NOT_EXIST = "Blog matching query does not exist."
STRING_VALIDATION_ERROR = "StringField only accepts string values"
