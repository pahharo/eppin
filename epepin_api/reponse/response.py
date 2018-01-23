'''
Created on Jan 16, 2017

@author: Asgard Team
'''
from flask import make_response
import json
from bson import ObjectId

class Response:

    def __init__(self):
        pass

    @staticmethod
    def _private_json_response(data_response, code):
        resp = make_response(data_response, code)
        resp.mimetype = 'application/json'
        resp.content_type = 'application/json'
        return resp

    @staticmethod
    def json_data(code, message, data_response=None, requirement=None):
        dict_response = {}
        dict_response["code"] = code
        dict_response["message"] = message
        dict_response = Response.fill_dict(data_response, dict_response, requirement)
        resp = Response._private_json_response(json.dumps(dict_response), code)
        return resp

    @staticmethod
    def fill_dict(data_response, dict_response, requirement=None):
        if data_response is not None:
            if isinstance(data_response, list):
                dict_response["requirements"] = []
                for document in data_response:
                    document["_id"] = str(document["_id"])
                    dict_response["requirements"].append(document)
            else:
                dict_response["requirements"] = data_response
            if requirement is not None:
                if not isinstance(requirement, (str, unicode)):
                    dict_response["requirements"]["_id"] = str(requirement.inserted_id)
                else:
                    dict_response["requirements"]["_id"] = requirement
            return dict_response
