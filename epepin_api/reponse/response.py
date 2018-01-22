'''
Created on Jan 16, 2017

@author: Asgard Team
'''
from flask import make_response
import json

class Response:

    def __init__(self):
        pass

    @staticmethod
    def _private_json_response(data, code):
        resp = make_response(data, code)
        resp.mimetype = 'application/json'
        resp.content_type = 'application/json'
        return resp

    @staticmethod
    def json_data(code, message, data, requirement = None):
        dict_response = {}
        dict_response["code"] = code
        dict_response["message"] = message
        dict_response["requirements"] = data
        if requirement is not None:
            dict_response["requirements"]["id"] = str(requirement.inserted_id)
        resp = Response._private_json_response(json.dumps(dict_response), code)
        return resp
