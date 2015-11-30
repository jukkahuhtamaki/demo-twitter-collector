# runcollector.py

import simplejson as json

with open('keychain.json') as f:
  keychain = json.load(f)

# Authenticating to Twitter API
from requests_oauthlib import OAuth1

def get_oauth():
  oauth = OAuth1(keychain['CONSUMER_KEY'],
              client_secret=keychain['CONSUMER_SECRET'],
              resource_owner_key=keychain['OAUTH_TOKEN'],
              resource_owner_secret=keychain['OAUTH_TOKEN_SECRET'])
  return oauth


auth = get_oauth()

# Twitter REST API: https://dev.twitter.com/rest/public
# Searching tweets through the API
# https://api.twitter.com/1.1/search/tweets.json?q=%40twitterapi

import requests
r = requests.get(url='https://api.twitter.com/1.1/search/tweets.json?q=%40twitterapi', auth=get_oauth())

print r.json().keys()

print len(r.json()['statuses'])

r = requests.get(url='https://api.twitter.com/1.1/search/tweets.json?q=pilvipalvelu&count=100', auth=get_oauth())
print len(r.json()['statuses'])

r = requests.get(url='https://api.twitter.com/1.1/search/tweets.json?q=6aika&count=100', auth=get_oauth())
print len(r.json()['statuses'])

with open('data/tweets-6aika.json','w') as f:
  json.dump(r.json(),f,indent=1)