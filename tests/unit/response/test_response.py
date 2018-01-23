import unittest
from epepin_api.reponse.response import Response
import bson
import io
from epepin_api.codes.codes import *
from epepin_api.codes.messages import *

class TestResponse(unittest.TestCase):

    def setUp(self):
        self.data = {
            "requirement_id": 1,
            "user_story": "story",
            "description": "description",
            "attributes": [
                {
                    "attr1": 1
                },
                {
                    "attr2": 2
                }
            ]
        }

        self.data_list = [
              {
                 "_id": bson.ObjectId("5a66f56207d8c33c2ea49b03"),
                 "user_story":"story",
                 "description":"description",
                 "attributes":[
                    {
                       "attr1":1
                    },
                    {
                       "attr2":2
                    }
                 ]
              },
              {
                 "_id":bson.ObjectId("5a66f56207d8c33c2ea49b05"),
                 "user_story":"story",
                 "description":"description",
                 "attributes":[
                    {
                       "attr1":1
                    },
                    {
                       "attr2":2
                    }
                 ]
              }
           ]

        self.requirement = io.StringIO()
        self.requirement.__setattr__("inserted_id",
                                     bson.ObjectId("5a66f56207d8c33c2ea49b03"))


    def test_fill_dict_with_requirement_ok(self):
        dict_response = {}
        dict_response["code"] = CODE_POST_OK
        dict_response["message"] = MSG_POST_OK
        dict_response = Response.fill_dict(self.data, dict_response, self.requirement)
        self.assertEqual(dict_response["requirements"], self.data)

    def test_fill_dict_without_requirement_ok(self):
        dict_response = {}
        dict_response["code"] = CODE_GET_OK
        dict_response["message"] = MSG_GET_OK
        dict_response = Response.fill_dict(self.data_list, dict_response, None)
        self.assertEqual(len(dict_response["requirements"]), 2)

if __name__ == '__main__':
    unittest.main()
