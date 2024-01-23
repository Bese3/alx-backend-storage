#!/usr/bin/env python3
"""
update school collection
"""


def update_topics(mongo_collection, name, topics):
    """
    The function updates the "topics" field in documents of a 
    MongoDB collection that match a given name.
    """
    mongo_collection.update_many({"name": name},
                                 {"$set": {"topics": topics}})
