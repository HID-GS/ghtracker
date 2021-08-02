from requests.auth import HTTPBasicAuth

import requests
import json

def getRepos(config, page=1):
    github = config['github']
    auth = HTTPBasicAuth(github['user'],github['token'])
    org = github['org']
    url = 'https://api.github.com/orgs/'
    per_page = github['per_page']
    params = {
            'page': page,
            'per_page': per_page
            }
    headers = {
            'Accept': 'application/vnd.github.v3+json'
            }
    req = requests.get(url + org + '/repos', params=params, auth=auth)
    results = json.loads(req.text)
    if len(results) == per_page:
        results.extend(getRepos(config, page+1))
    return results

def getRepo(config, repo):
    github = config['github']
    auth = HTTPBasicAuth(github['user'],github['token'])
    url = repo['url']
    headers = {
            'Accept': 'application/vnd.github.v3+json'
            }
    req = requests.get(url, auth=auth)
    return json.loads(req.text)
