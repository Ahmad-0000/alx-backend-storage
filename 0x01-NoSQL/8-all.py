#!/usr/bin/env python3
"""
9th task's solution
"""


def list_all(mongo_collection):
    """Returns a list of documents found in a pymongo collection object"""
    collist = []
    for i in mongo_collection.find():
        collist.append(i)
    return collist
