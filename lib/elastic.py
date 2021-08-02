import json
import requests
from datetime import datetime

def send(config, data):
    data['@timestamp'] = datetime.now().astimezone().isoformat()
    data['@version'] = 1
    headers = {
            'Content-Type': 'application/json',
            'Content-Length': str(len(json.dumps(data))),
            'Authorization': 'Basic ' + config['elastic']['auth']
            }
    url = config['elastic']['url'] + '/ghtracker-' + data['name'].lower() + '/_doc'
    return requests.post(url, headers=headers, json=data)

