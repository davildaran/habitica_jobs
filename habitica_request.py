import os
import requests
import json

from common.constants import HABITICA_API_URL
from secret import user_id, api_token


class HabitRequest:

    def __init__(self):

        self.user_id = user_id
        self.api_token = api_token
        self.url = HABITICA_API_URL

    def set_auth(self, user_id, api_token):
        return {'Content-Type': 'application/json',
                'x-api-user': user_id,
                'x-api-key': api_token}

    def get_user_profile(self):
        # get the authenticated user's profile
        r = requests.get(url=os.path.join(self.url, 'user'),
                         headers=self.set_auth(self.user_id,
                                               self.api_token))
        # check response status code
        if r.status_code == 200:
            print(f'Successfully got user profile info!\n')
            data = json.loads(r.text)
            with open('user_profile.json', 'w+') as handler:
                handler.write(json.dumps(data, sort_keys=True, indent=4))
        else:
            print(f'Error getting user profile info!\n'
                  f'{r.text}')
        return r


if __name__ == "__main__":
    habitica = HabitRequest()
    habitica.set_auth(user_id, api_token)
    habitica.get_user_profile()
