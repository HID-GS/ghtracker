import base64
import os
import sys
import yaml

def Config():

    if os.path.exists('config.yaml'):
        print('from file')
        raw = open('config.yaml','r').read()
    else:
        print('from variable')
        raw = base64.b64decode(os.environ['GHCONFIG'])
    return yaml.safe_load(raw)

