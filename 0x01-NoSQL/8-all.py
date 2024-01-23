#!/usr/bin/env python3
"""
List all documents in Python
"""
# from typing import List


def list_all(mongo_collection):
    """
    The function "list_all" returns all documents in a MongoDB collection.
    """
    return mongo_collection.find()
