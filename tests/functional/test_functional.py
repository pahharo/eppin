import requests
import unittest


class TestFunctional(unittest.TestCase):

    def setUp(self):
        pass

    def test_post_requirement(self):
        response = requests.post('http://localhost:8085/v1/requirement', None,
                                 {"requirement_id": "xyz","user_story": "xyz",
                                  "description": "xyz"})
        print response
        self.assertEqual(response.status_code, 201)