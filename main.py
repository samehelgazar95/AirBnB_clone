#!/usr/bin/python3
from models.base_model import BaseModel
import datetime


b = BaseModel()
b.created_at = datetime.datetime(2024, 1, 1, 0, 0, 0, int(0.123456 * 1000000))
expected_dict = {
    'id': b.id,
    'created_at': '2024-01-01T00:00:01.123456',
    'updated_at': b.updated_at.isoformat(),
    '__class__': b.to_dict()['__class__']
}

print(expected_dict)
print(b.to_dict())
