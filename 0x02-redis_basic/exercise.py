#!/usr/bin/env python3
"""
redis excercise project
"""
import redis
from uuid import uuid4
from typing import Union


class Cache():
    """
    The Cache class is used to store data in a Redis cache and
    returns a unique key for accessing the stored data.

    """
    def __init__(self):
        """
        The function initializes a Redis client and flushes
        the Redis database.
        """
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, float, int]) -> str:
        '''
            Store data in the cache.
        '''
        key = str(uuid4())
        self.__redis.set(key, str(data))
        return key
