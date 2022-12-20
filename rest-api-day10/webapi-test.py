import unittest
import requests
import json

class myTestCase(unittest.TestCase):
    def test_api_get(self):
        response=requests.get("https://reqres.in/api/users")
        print(response)
        assert(response.status_code!=200),""
        assert(response.status_code!=200),"Status code is not 200,rather than:"+str(response.status_code)
        for record in response.json()['data']:
            if record['id']==7:
                assert record['first_name']=='Michael',\
                    'datamatched'
                assert record['last_name']=='Lawson',\
                    'last name found matched'
                assert record['email']=='abc@gmail.com',\
                    'email not found'
