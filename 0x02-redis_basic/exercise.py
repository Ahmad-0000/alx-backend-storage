#!/usr/bin/env python3
"""
Caching module
"""
import redis
import uuid
from typing import Union, Optional


class Cache():
    """To perform caching operations"""

    def __init__(self: 'Cache') -> None:
        """Inistatciating an object for cache operations"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Storing data into redis server"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn=None) -> Optional[bytes]:
        """Getting data from redis server"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self) -> Optional[int]:
        """Returns a string"""
        try:
            return str(self._redis.get(key))
        except ValueError:
            return None

    def get_int(self):
        """Returns an int"""
        try:
            return int(self._redis.get(key))
        except ValueError:
            return None
