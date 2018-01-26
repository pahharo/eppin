'''
Created on Jan 16, 2017

@author: Asgard Team
'''

from flask import Blueprint, render_template
from flask import request
import copy
import io
from epepin_api import utils
from epepin_api.codes import codes
from epepin_api.codes.messages import *
from epepin_api.database import database
import bson
from epepin_api.exceptions.epepin_exceptions import *


apiv1 = Blueprint('apiv1', __name__, template_folder="../templates")


def database_connection():
    cfg = utils.get_config()
    db = database.Database(cfg.epepin_db_endpoint, cfg.epepin_db_port)
    return db

@apiv1.route('/')
def showIndex():
    return render_template('list.html')


@apiv1.route('/requirement', methods=['GET'])
def get_requirements():
    status_code = CODE_GET_OK
    message = MSG_GET_OK
    requirements = None
    try:
        db = database_connection()
        connection = db.connection()
        requirements = db.get_requirements(connection)
    except EpepinException as ex:
        status_code = ex.get_status_code()
        message = ex.get_error_message()
    return Response.json_data(status_code, message, requirements, None)


@apiv1.route('/requirement/<string:requirement_id>', methods=['GET'])
def get_requirement(requirement_id):
    status_code = CODE_GET_OK
    message = MSG_GET_OK
    requirement = None
    try:
        db = database_connection()
        connection = db.connection()
        requirement = db.get_requirement(connection, requirement_id)
    except EpepinException as ex:
        status_code = ex.get_status_code()
        message = ex.get_error_message()
    return Response.json_data(status_code, message, requirement, requirement_id)


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
    status_code = CODE_PUT_OK
    message = MSG_PUT_OK
    try:
        data = request.get_json()
        input_data = copy.deepcopy(data)
        db = database_connection()
        connection = db.connection()
        db.update_requirement(connection, requirement_id, data)
    except EpepinException as ex:
        status_code = ex.get_status_code()
        message = ex.get_error_message()
    return Response.json_data(status_code, message, input_data, requirement_id)


@apiv1.route('/requirement/<string:requirement_id>', methods=['DELETE'])
def delete_requirement(requirement_id):
    status_code = CODE_DELETE_OK
    message = MSG_DELETE_OK
    try:
        db = database_connection()
        connection = db.connection()
        db.delete_requirement(connection, requirement_id)
    except EpepinException as ex:
        status_code = ex.get_status_code()
        message = ex.get_error_message()
    return Response.json_data(status_code, message, None, requirement_id)

@apiv1.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response