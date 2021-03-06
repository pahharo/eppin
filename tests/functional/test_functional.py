import requests
import unittest
import json


class TestFunctional(unittest.TestCase):

    def setUp(self):
        pass

    def test_post_requirement(self):
        response = requests.post('http://localhost:8085/v1/requirement', None,
                                 {"user_story": "xyz",
                                  "description": "xyz"})
        dict_response = json.loads(response._content)
        requests.delete('http://localhost:8085/v1/requirement/%s' %
                        dict_response["requirements"]["_id"])
        self.assertEqual(response.status_code, 201)

    def test_put_requirement(self):
        post_response = requests.post('http://localhost:8085/v1/requirement', None,
                                 {"user_story": "xyz",
                                  "description": "xyz"})
        self.assertEqual(post_response.status_code, 201)

        dict_post_response = json.loads(post_response._content)
        put_response = requests.put('http://localhost:8085/v1/requirement/%s' %
                                dict_post_response["requirements"]["_id"],
                                json={"user_story": "abc","description": "retarded"})
        self.assertEqual(put_response.status_code, 200)

        delete_response = requests.delete('http://localhost:8085/v1/requirement/%s' %
                                          dict_post_response["requirements"]["_id"])
        self.assertEqual(delete_response.status_code, 204)


    def test_get_requirements(self):
        response = requests.post('http://localhost:8085/v1/requirement', None,
                                 {"user_story": "xyz",
                                  "description": "xyz", "attributes": ["attr1", "attr2"]})
        dict_response = json.loads(response._content)
        response = requests.get('http://localhost:8085/v1/requirement', None)
        requests.delete('http://localhost:8085/v1/requirement/%s' %
                        dict_response["requirements"]["_id"])
        self.assertEqual(response.status_code, 200)

    def test_get_requirement(self):
        response = requests.post('http://localhost:8085/v1/requirement', None,
                                 {"user_story": "xyz",
                                  "description": "xyz", "attributes": ["attr1", "attr2"]})
        dict_response = json.loads(response._content)
        response = requests.get('http://localhost:8085/v1/requirement/%s'
                                %dict_response["requirements"]["_id"], None)
        requests.delete('http://localhost:8085/v1/requirement/%s' %
                        dict_response["requirements"]["_id"])
        self.assertEqual(response.status_code, 200)
