from epepin_api.exceptions.epepin_exceptions import EpepinException
from epepin_api.reponse.response import Response
from epepin_api.codes.codes import *

class RequestException(EpepinException):

    def __init__(self, code, msg=None):
        super(RequestException, self).__init__(CODE_DB_ERROR,
                                          "DB error %s" %msg,
                                          Response.
                                          json_data(CODE_DB_ERROR, msg,
                                                    None)
                                          )
