import os
import requests

from habitica_request import HabitRequest


class BuyHealthPotion(HabitRequest):

    def __init__(self):
        super().__init__()

    def buy_health_potion(self, profile):
        # check if health is not low, don't buy a health potion
        if not profile.json()['data']['flags']['warnedLowHealth']:
            print(f'Health is not low - aborting health potion purchase!')
            return

        # otherwise, continue with the buy health potion request
        r = requests.post(url=os.path.join(self.url, 'user', 'buy-health-potion'),
                          headers=self.set_auth(self.user_id, self.api_token))

        # check response status code
        if r.status_code == 200:
            print(f'Successfully bought a health potion!\n'
                  f'{r.text}')
        else:
            print(f'Error buying a health potion!\n'
                  f'{r.text}')


if __name__ == "__main__":
    buy_health_potion = BuyHealthPotion()
    profile_info = buy_health_potion.get_user_profile()
    buy_health_potion.buy_health_potion(profile_info)
