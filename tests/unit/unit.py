import unittest
import requests
import json


class TestFlaskApiRequestRequirement(unittest.TestCase):

    def test_get_all_requirements(self):
        response = requests.get('http://localhost:8085/v1/requirement')
        self.assertEqual(response.json(), {'hello': 'world'})

    def test_get_requirement(self):
        req1 = "req1"
        response = requests.get('http://localhost:8085/v1/requirement/%s' % req1)
        self.assertEqual(response.json(), {'hello': '%s' % req1})

    def test_create_requirement(self):
        response = requests.post('http://localhost:8085/v1/requirement', None,
                                 {"requirement_id": "xyz","user_story": "xyz",
                                  "description": "xyz"})
        self.assertEqual(response.json(), {"rp": "xyz", "up": "xyz", "du": "xyz"})

    def test_update_requirement(self):
        req1 = "req1"
        response = requests.put('http:/'
                                '/localhost:8085/v1/requirement/%s' % req1,
                                data=json.dumps({'requirement_id':'xyz','user_story':'xyz','description':'xyz'}))
        print response
        self.assertEqual(response.json(), {"ru": "%s", "uu": "xyz", "du": "xyz" % req1})


if __name__ == "__main__":
    unittest.main()
