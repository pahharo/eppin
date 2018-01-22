import unittest
from epepin_api.database.database import *


class TestDatabase(unittest.TestCase):
    # To pass this tests it is needed a MongoDB called
    # Requirement and a Collection inside called Requirements
    mongo_db = Database('localhost', 27017)
    db_connection = mongo_db.connection()

    def test_insert_requirement_ok(self):
        requirement = self.mongo_db.insert_requirement(self.db_connection,
                                                       {'hello': 'world'})
        self.mongo_db.delete_requirement(self.db_connection,
                                         {'hello': 'world'})
        self.assertEqual(requirement.acknowledged, True)

    def test_get_requirement_ok(self):
        id = self.mongo_db.insert_requirement(self.db_connection,
                                         {'hello': 'world'}).inserted_id
        requirement = self.mongo_db.get_requirement(self.db_connection,
                                                    id)
        self.mongo_db.delete_requirement(self.db_connection,
                                         {'hello': 'world'})
        self.assertEqual(requirement.get('hello'), 'world')


    def test_update_requirement_ok(self):
        requirement = self.mongo_db.insert_requirement(self.db_connection,
                                                       {'hello': 'world',
                                                        'requirement_id': '1'})
        requirement = self.mongo_db.update_requirement(self.db_connection,
                                                       requirement.inserted_id,
                                                       {'hello': 'everybody'})
        self.mongo_db.delete_requirement(self.db_connection, {'hello': 'everybody'})
        self.assertEqual(requirement.acknowledged, True)

    def test_db_connection_timeout(self):
        error_db = Database("7.7.7.7", 22222)
        db = error_db.connection()
        with self.assertRaises(DBConnectionException):
            error_db.get_requirement(db, '5a61df558c1b672d15bb85f7')


if __name__ == '__main__':
    unittest.main()
