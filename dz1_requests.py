import requests
import json
import os
username = 'EkaterinaYakimova'
token = os.environ.get("GITHUB_TOKEN")
repos = requests.get('https://api.github.com/user/repos', auth=(username, token))


with open('data1.json', 'w') as f:
    json.dump(repos.json(), f)

