import json

import requests


def get_github_users(users):
    users_list=[]
    for user in users:
        response = requests.get(f'https://api.github.com/users/{user}')
        response2 = requests.get(f'https://api.github.com/users/{user}/repos')
        result = {
            'login': response.json()['login'],
            'public_repos': response.json()['public_repos'],
            'repositories': [repo['name'] for repo in response2.json()]
        }


        users_list.append(result)
        print(users_list)

    return users_list


if __name__ == '__main__':
    users = ['Nikodim26']
    result = json.dumps(get_github_users(users),indent=4)
    print(result)
