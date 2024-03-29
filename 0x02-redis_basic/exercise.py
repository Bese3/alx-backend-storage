#!/usr/bin/env python3
"""
redis excercise project
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    The `count_calls` function is a decorator that increments a
    counter in Redis and then calls the original method with the
    given arguments.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        The wrapper function increments a counter in Redis
        and then calls the original method with the given arguments.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    The `call_history` function is a decorator that logs the input
    and output of a method call using Redis.
    """
    key = method.__qualname__
    input = key + ":inputs"
    output = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        The wrapper function logs the input and output of a method
        call using Redis.
        """
        self._redis.rpush(input, str(args))
        m = method(self, *args, **kwargs)
        self._redis.rpush(output, str(m))
        return m
    return wrapper


def replay(method: Callable) -> None:
    """
    The `replay` function retrieves and prints information about a
    method's previous calls and their inputs and outputs.
    """
    key = method.__qualname__
    r = redis.Redis()
    print(f"{key} was called {r.get(key).decode('utf-8')} times:")
    inputs = r.lrange(f"{key}:inputs", 0, -1)
    outputs = r.lrange(f"{key}:outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print(f"{key}(*{i.decode('utf-8')}) -> {o.decode('utf-8')}")


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
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
            Store data in the cache.
        '''
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        The function retrieves a value from Redis using a given
        key and applies a function to the value if provided.
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, value: str) -> str:
        """
        The function `get_str` takes a value and decodes it
        from UTF-8 encoding to a string.
        """
        return value.decode('utf-8')

    def get_int(self, value: str) -> int:
        """
        The function `get_int` takes a value, decodes it from UTF-8
        to a string, tries to convert it to an integer, and returns
        the integer value. If the conversion fails, it returns 0.
        """
        try:
            i = int(value.decode('utf-8'))
        except Exception:
            i = 0
        return i
