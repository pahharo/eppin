import unittest
from epepin_api.exceptions.db_exceptions import DBException


class TestDBExceptions(unittest.TestCase):
    def test_db_exception_ok(self):
        result = DBException("Error connecting to DB")
        self.assertEqual(result.status_code, 500)



if __name__ == '__main__':
    unittest.main()
