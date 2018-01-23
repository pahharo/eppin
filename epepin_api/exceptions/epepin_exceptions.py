from epepin_api.reponse.response import Response
from epepin_api.codes.codes import *

class EpepinException(Exception):

    def __init__(self, error_message):
        super(EpepinException, self).__init__(error_message)
        self.error_message = error_message
        self.status_code = CODE_SERVICE_UNAVAILABLE

    def __init__(self, status_code, error_message):
        super(EpepinException, self).__init__(error_message)
        self.error_message = error_message
        self.status_code = status_code

    def get_error_message(self):
        return self.error_message

    def get_status_code(self):
        return self.status_code