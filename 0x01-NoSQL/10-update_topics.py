#!/usr/bin/env python3
"""
11th task's solution
"""


def update_topics(mongo_collection, name, topics):
    """Updating a topic list in a document with a certain name"""
    result = mongo_collection.update_many(
                {"name": name},
                {"$set": {"topics": topics}}
    )
