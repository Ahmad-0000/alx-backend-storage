#!/usr/bin/env python3
"""
12th task's solution
"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list of school names having a specific topic"""
    doclist = []
    for doc in mongo_collection.find():
        if topic in doc["topics"]:
            doclist.append(doc)
    return doclist
