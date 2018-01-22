import unittest
from epepin_api.exceptions.db_exceptions import DBException


class TestDBExceptions(unittest.TestCase):
    def test_db_exception_ok(self):
        DBException("{'hello': 'world'}","Error connecting to DB")
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
