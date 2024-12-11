#!/usr/bin/env python3
""" Insert a document in Python """

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    :param mongo_collection: pymongo collection object
    :param kwargs: key-value pairs to insert as document
    :return: the new _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
