from pymongo import MongoClient
from pymongo.errors import *
from bson.objectid import ObjectId
from epepin_api.exceptions.db_exceptions import *


class Database(object):

    def __init__(self, endpoint, port):
        self.endpoint = endpoint
        self.port = port

    def connection(self):
        try:
            client = MongoClient(self.endpoint, self.port, serverSelectionTimeoutMS=5000)
            db = client.Requirement
        except Exception as e:
            DBException(e.message)
        return db

    @classmethod
    def insert_requirement(cls, database, data):
        try:
            requirement = database.Requirements.insert_one(data)
        except NetworkTimeout as e:
            raise
        except Exception as e:
            raise DBException(e.message)
        return requirement

    @classmethod
    def get_requirements(cls, database):
        return database.Requirements.find()

    @classmethod
    def get_requirement(cls, database, requirement_id):
        try:
            requirement = database.Requirements.find_one({'_id': ObjectId(requirement_id)})
        except Exception as e:
            raise DBException(e.message)
        return requirement

    @classmethod
    def update_requirement(cls, database, requirement_id, data):
        try:
            requirement = database.Requirements.update_one({'_id':ObjectId(requirement_id)},
                                                           {'$set': data})
        except Exception as e:
            raise DBException(e.message)
        return requirement

    @classmethod
    def delete_requirement(cls, database, condition):
        try:
            requirement = database.Requirements.delete_many(condition)
        except Exception as e:
            raise DBException(e.message)
        return requirement
