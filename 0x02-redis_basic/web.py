#!/usr/bin/env python3
"""
Web scrapper
"""
import redis
import requests


def get_page(url: str) -> str:
    """Getting a resource located in url"""
    r = redis.Redis()
    key = f"count:{{{url}}}"
    r.incr(key, 1)
    r.expire(key, 10)
    fun = requests.request
    result = fun('GET', url)
    return result.text
