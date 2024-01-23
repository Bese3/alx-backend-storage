#!/usr/bin/env  python3
"""
searching by a string in array
"""


def schools_by_topic(mongo_collection, topic):
    """
    The function `schools_by_topic` takes a MongoDB collection
    and a topic as input, and returns all documents in the collection
    that have the specified topic in their "topics" field.
    """
    return mongo_collection.find({"topics": {"$elemMatch": {"$eq": topic}}})
