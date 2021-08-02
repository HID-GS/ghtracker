import sys
import yaml
from lib.config import Config
from lib import elastic
from lib import github

config = Config()

results = github.getRepos(config)
total = len(results)
gone = 0
for result in results:
    gone += 1
    print('fetching ' + result['name'] + " - " + str(gone) + "/" + str(total))
    repo = github.getRepo(config, result)
    print('sending data to elastic')
    elastic.send(config, repo)

