from epepin_api.exceptions.epepin_exceptions import EpepinException
from epepin_api.reponse.response import Response
from epepin_api.codes.codes import *

class DBException(EpepinException):

    def __init__(self, msg=None):
        super(DBException, self).__init__(CODE_DB_ERROR,
                                          "DB error %s" %msg,
                                          )

