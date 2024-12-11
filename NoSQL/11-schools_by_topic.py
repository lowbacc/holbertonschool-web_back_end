#!/usr/bin/env python3
""" Schools by topic in Python """


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic
    :param mongo_collection: pymongo collection object
    :param topic: topic searched
    :return: list of schools having the specific topic
    """
    return list(mongo_collection.find({"topics": topic}))
