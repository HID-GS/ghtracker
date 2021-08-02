#!/usr/bin/env bash

if [ "${GH_TOKEN:-no}" == "no" ]; then
  echo "missing GH_TOKEN variable. exiting..."
  exit 1
fi

if [ "${GH_USER:-no}" == "no" ]; then
  echo "missing GH_USER variable. exiting..."
  exit 1
fi

if [ "${GH_ORG:-no}" == "no" ]; then
  echo "missing GH_ORG variable. exiting..."
  exit 1
fi

mkdir -p data

curl -s -u ${GH_USER}:${GH_TOKEN}  -H "Accept: application/vnd.github.v3+json"   https://api.github.com/orgs/${GH_ORG}/repos?page=1 > data/org-repos-1.json
curl -s -u ${GH_USER}:${GH_TOKEN}  -H "Accept: application/vnd.github.v3+json"   https://api.github.com/orgs/${GH_ORG}/repos?page=2 > data/org-repos-2.json
curl -s -u ${GH_USER}:${GH_TOKEN}  -H "Accept: application/vnd.github.v3+json"   https://api.github.com/orgs/${GH_ORG}/repos?page=3 > data/org-repos-3.json
curl -s -u ${GH_USER}:${GH_TOKEN}  -H "Accept: application/vnd.github.v3+json"   https://api.github.com/orgs/${GH_ORG}/repos?page=4 > data/org-repos-4.json
curl -s -u ${GH_USER}:${GH_TOKEN}  -H "Accept: application/vnd.github.v3+json"   https://api.github.com/orgs/${GH_ORG}/repos?page=5 > data/org-repos-5.json

grep '^    "url"' org-repo-*.json | while read raw; do
  url="$(echo $raw | sed 's/.*"url"\: "\([^"]*\)".*/\1/g')"
  repo="$(echo $url | sed 's#.*/##g')"

  echo "fetching $repo"
  curl -s -u ${GH_USER}:${GH_TOKEN}  -H "Accept: application/vnd.github.v3+json"   $url > data/org-repo__${repo}.json
done
