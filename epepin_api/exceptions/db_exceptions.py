

class DBException(BaseException):

    def __init__(self, requirement,msg=None):
        if msg is None:
            msg = "DB exception with %s" %requirement
        super(DBException, self).__init__(msg)
        self.requirement = requirement


class DBConnectionException(Exception):
    def __init__(self, msg=None):
        if msg is None:
            msg = "DB exception: connection to db failed"
        super(DBConnectionException, self).__init__(msg)

