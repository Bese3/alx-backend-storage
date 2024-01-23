#!/usr/bin/env python3
"""
Insert a document in Python
"""


def insert_school(mongo_collection, **kwargs):
    """
    The function `insert_school` inserts a new record into a MongoDB
    collection with the provided keyword arguments.
    """
    new_record = mongo_collection.insert_one(kwargs)
    return new_record.inserted_id
