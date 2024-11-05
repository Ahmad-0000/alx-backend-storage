#!/usr/bin/env python3
"""
10th task's solution
"""


def insert_school(mongo_collection, **kwargs):
    """Inserting a document in a collection"""
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
