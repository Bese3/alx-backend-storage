#!/usr/bin/env python3
"""
nignx server logs
"""
from pymongo import MongoClient


def main():
    """
    The main function connects to a MongoDB database,
    retrieves logs from the 'nginx' collection.
    """
    db = MongoClient('mongodb://127.0.0.1:27017')
    my_coll = db.logs.nginx
    print(f"{my_coll.count_documents({})} logs")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print("Methods:")
    for m in methods:
        method_log = my_coll.count_documents({"method": {"$eq": m}})
        print(f"\tmethod {m}: {method_log}")
    status = my_coll.count_documents({"path": {"$eq": "/status"}})
    print(f"{status} status check")


if __name__ == '__main__':
    main()
