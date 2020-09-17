import os
import requests
import argparse
import json

from habitica_request import HabitRequest


class Tasks(HabitRequest):

    def __init__(self):
        super().__init__()
        self.requested_tasks = {}
        self.url = os.path.join(self.url, 'tasks')

    def get_tasks(self):
        r = requests.get(url=os.path.join(self.url, 'user'),
                         headers=self.set_auth(self.user_id, self.api_token),
                         params=self.requested_tasks)

        # check response status code
        if r.status_code == 200:
            print(f'Success issuing task request!\n')
            data = json.loads(r.text)
            with open('user_tasks.json', 'w+') as handler:
                handler.write(json.dumps(data, indent=4))
        else:
            print(f'Error issuing task request\n'
                  f'{r.text}')

        return r

    # def check dailys ?
    # if dailys aren't completed by 9PM, email and text reminders?

    @staticmethod
    def main():

        parser = argparse.ArgumentParser()
        parser.add_argument("--habits", "-b", dest="habits", action="store_true",
                            help="flag to query Task type 'habit'")
        parser.add_argument("--dailys", "-d", dest="dailys", action="store_true",
                            help="flag to query Task type 'daily'")
        parser.add_argument("--todos", "-t", dest="todos", action="store_true",
                            help="flag to query Task type 'todos'")
        parser.add_argument("--rewards", "-r", dest="reward", action="store_true",
                            help="flag to query Task type 'reward'")
        args = parser.parse_args()
        tasks = Tasks()
        tasks.requested_tasks = vars(args)
        tasks.get_tasks()
        sum = 1


if __name__ == "__main__":
    tasks = Tasks()
    tasks.main()
    # tasks.get_tasks()
