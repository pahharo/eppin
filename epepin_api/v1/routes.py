'''
Created on Jan 16, 2017

@author: Asgard Team
'''

from flask import Blueprint
from flask import request

from epepin_api import utils
from epepin_api.codes import codes
from epepin_api.database import database
from epepin_api.reponse import response


apiv1 = Blueprint('apiv1', __name__)


def database_connection():
    cfg = utils.get_config()
    db = database.Database(cfg.epepin_db_endpoint, cfg.epepin_db_port)
    return db


@apiv1.route('/requirement', methods=['GET'])
def get_requirements():
    try:
        db = database_connection()
        connection = db.connection()
        requirements = db.get_requirements(connection)
        return json_response(codes.CODE_GET_OK)
    except Exception as ex:
        return json_response(codes.CODE_BAD_REQ_ERROR)


@apiv1.route('/requirement/<string:requirement_id>', methods=['GET'])
def get_requirement(requirement_id):
    try:
        db = database_connection()
        connection = db.connection()
        requirement = db.get_requirement(connection)
        json = '{"hello": "%s"}' % requirement_id
        return json_response(codes.CODE_GET_OK)

    except Exception as ex:
        return json_response(codes.CODE_BAD_REQ_ERROR)


@apiv1.route('/requirement', methods=['POST'])
def create_requirement():
    try:
        data = request.get_json()
        requirement_id = data['requirement_id']
        user_story = data['user_story']
        description = data['description']
        json = '{"rp": "%s", "up": "%s", "du": "%s"}' % (requirement_id, user_story, description)
        db = database_connection()
        connection = db.connection()
        requirement = db.insert_requirement(connection, data)
        return response.Response.json_data(codes.CODE_GET_OK, "Created successfully", requirement)
    except Exception as ex:
        return response.Response.json_data(codes.CODE_BAD_REQ_ERROR, ex.message)


@apiv1.route('/requirement/<string:requirement_id>', methods=['PUT'])
def update_requirement(requirement_id):
    try:
        data = request.get_json()
        user_story = data['user_story']
        description = data['description']
        json = '{"ru": "%s", "uu": "%s", "du": "%s"}' % (requirement_id, user_story, description)
        #db = database_connection()
        #connection = db.connection()
        #requirement = db.update_requirement(connection, data)
        return json_response(codes.CODE_GET_OK)
    except Exception as ex:
        return json_response(codes.CODE_BAD_REQ_ERROR)