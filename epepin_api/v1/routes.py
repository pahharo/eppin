'''
Created on Jan 16, 2017

@author: Asgard Team
'''

from flask import Blueprint
from flask import request
import copy

from epepin_api import utils
from epepin_api.codes import codes
from epepin_api.codes.messages import *
from epepin_api.database import database
from epepin_api.reponse.response import *
from epepin_api.exceptions.epepin_exceptions import *


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
        return Response.json_data(codes.CODE_GET_OK)
    except Exception as ex:
        return Response.json_data(codes.CODE_GET_OK)


@apiv1.route('/requirement/<string:requirement_id>', methods=['GET'])
def get_requirement(requirement_id):
    try:
        db = database_connection()
        connection = db.connection()
        requirement = db.get_requirement(connection)
        json = '{"hello": "%s"}' % requirement_id
        return Response.json_data(codes.CODE_GET_OK)

    except Exception as ex:
        return Response.json_data(codes.CODE_BAD_REQ_ERROR)


@apiv1.route('/requirement', methods=['POST'])
def create_requirement():
    status_code = CODE_POST_OK
    message = MSG_POST_OK
    requirement = None
    try:
        data = request.get_json()
        input_data = copy.deepcopy(data)
        db = database_connection()
        connection = db.connection()
        requirement = db.insert_requirement(connection, data)
    except EpepinException as ex:
        status_code = ex.get_status_code()
        message = ex.get_error_message()
    return Response.json_data(status_code, message, input_data, requirement)



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
        return Response.json_data(codes.CODE_GET_OK)
    except Exception as ex:
        return Response.json_data(codes.CODE_BAD_REQ_ERROR)