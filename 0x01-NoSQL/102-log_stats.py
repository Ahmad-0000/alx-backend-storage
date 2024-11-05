#!/usr/bin/env python3
"""
13th task's solution
"""
import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient()
    db = client.logs
    col = db.nginx

    print(f'{col.count_documents({})} logs\nMethods:')
    print(f'\tmethod GET: {col.count_documents({"method": "GET"})}')
    print(f'\tmethod POST: {col.count_documents({"method": "POST"})}')
    print(f'\tmethod PUT: {col.count_documents({"method": "PUT"})}')
    print(f'\tmethod PATCH: {col.count_documents({"method": "PATCH"})}')
    print(f'\tmethod DELETE: {col.count_documents({"method": "DELETE"})}')
    status_check = col.count_documents({"method": "GET", "path": "/status"})
    print(f'{status_check} status check')
    print("IPs:")
    
    pipeline = [
            {"$group": {"_id": "$ip", "totalReq": {"$sum": 1}}},
            {"$sort": {"totalReq": -1}},
            {"$limit": 10}
    ]

    documents = list(col.aggregate(pipeline))
    for doc in documents:
        print("\t{}: {}".format(doc.get("_id"), doc.get("totalReq")))
    client.close()
