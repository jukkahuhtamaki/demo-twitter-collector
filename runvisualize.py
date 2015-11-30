# runvisualize.py

import simplejson as json

with open('data/tweets-6aika.json','r') as f:
  tweets = json.load(f)

# Looking into a tweet
tweet = tweets['statuses'][0]
print tweet['user']['screen_name']
print tweet['entities']['user_mentions']
for user in tweet['entities']['user_mentions']:
  print user['screen_name']

# Tweets to tabular format
import pandas as pd
rows = list()
for tweet in tweets['statuses']:
  # print tweet['text']
  rows.append([tweet['text']])
  for mentioned in tweet['entities']['user_mentions']:
    print tweet['user']['screen_name'],'-',mentioned['screen_name']

    # Create a row for each tweet
    # Note: one-to-many connections are much more easy to solve taking
    # an interactive computing approach to visual analytics!

import networkx as nx
network = nx.DiGraph()
print 

for tweet in tweets['statuses']:
  # print tweet['text']
  rows.append([tweet['text']])
  for mentioned in tweet['entities']['user_mentions']:
    user_from = tweet['user']['screen_name'].lower()
    user_to = mentioned['screen_name'].lower()
    if not network.has_edge(user_from,user_to):
      network.add_edge(user_from,user_to,weight=0)
    network[user_from][user_to]['weight'] += 1 

nx.readwrite.gexf.write_gexf(network,'data/network.gexf',
  encoding='utf-8',version='1.2draft')


# df = pd.DataFrame(rows)
# df.to_csv('data/tweets-6aika.csv',encoding='utf-8')