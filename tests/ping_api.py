import requests
import os
import json

# from common import constants
# from secret import user_id, api_key

HABITICA_API_URL = "https://habitica.com/api/v3"
user_id = "d"
api_key = "b"

def set_auth(_user_id, _api_key):
	return {'Content-Type': 'application/json',
			'x-api-user': _user_id,
			'x-api-key': _api_key}


def test_habitica_api_status():
	r = requests.get(url=os.path.join(HABITICA_API_URL, 'status'),
					headers=set_auth(user_id, api_key))
	assert r.status_code == 200
	data = json.loads(r.text)
	assert data['data']['status'] == 'up'
	assert data['success']
	print('API Up status test passed')


if __name__ == "__main__":
	test_habitica_api_status()
