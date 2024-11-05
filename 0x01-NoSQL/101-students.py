#!/usr/bin/env python3
"""
2nd advanced task's solution
"""


def top_students(mongo_collection):
    """Returns students documents ordered by top average scores"""
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": 
            {
                "_id": "$_id",
                "name" : {"$first": "$name"},
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))
