#!/usr/bin/env python3
"""
12th task's solution
"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list of school documentss having a specific topic"""
    scls = mongo_collection.find({"topics": topic})
    return scls
