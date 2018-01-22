'''
Created on Jan 16, 2017

@author: Asgard Team
'''
from flask import make_response


def _private_json_response(data, code):
    resp = make_response(data, code)
    resp.mimetype = 'application/json'
    resp.content_type = 'application/json'
    return resp


class Response:

    def __init__(self):
        pass

    @staticmethod
    def json_data(code, message, requirement):
        json = '{"code": "%s", "message": "%s", "requirement": "%s"}' % (code, message, requirement)
        resp = _private_json_response(json, code)
        return resp
