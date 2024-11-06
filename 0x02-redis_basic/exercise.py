#!/usr/bin/env python3
"""
Caching module
"""
import redis
import uuid
from typing import Union


class Cache():
    """To perform caching operations"""

    def __init__(self: 'Cache') -> None:
        """Inistatciating an object for cache operations"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self: 'Cache', data: Union[str, bytes, float, int]) -> str:
        """Storing data into redis server"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
