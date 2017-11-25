# -*- coding: utf-8 -*-

import glob
import simplejson as json
import pandas as pd
# from ttp import ttp
import os
# import xlrd

# Twitter text python parser:
# https://github.com/edburnett/twitter-text-python
# parser = ttp.Parser()

def users_mentioned(tweet):
  # print tweet
  users = list()
  if pd.notnull(tweet):
    # for user in parser.parse(tweet.decode('utf-8')).users:
    # print(tweet)
    try:
        for user in parser.parse(tweet).users:
        # for user in parser.parse(tweet.encode('utf-8').decode('utf-8')).users:
          users.append(user.lower())
    except UnicodeError:
        print('Error when processing tweet: ' )
        print(tweet)
  return ','.join(users)

def hashtags(tweet):
  # print tweet
  hashtags = list()
  if pd.notnull(tweet):
    # for user in parser.parse(tweet.decode('utf-8')).users:
    # print(tweet)
    try:
        for hashtag in parser.parse(tweet).tags:
        # for hashtag in parser.parse(tweet.encode('utf-8').decode('utf-8')).tags:
          hashtags.append(hashtag.lower())
    except UnicodeError:
        print('Error when processing tweet: ' )
        print(tweet)
  return ','.join(hashtags)

df_all = pd.DataFrame()
tweets = dict()
tweets['statuses'] = list()
for fname in glob.glob('data/tweets/*.json'):
    print(fname)
    # csv_fname = 'data/01-batch-csv/%s.csv' % (fname.split('/')[-1].split('.')[0])
    # df_batch = pd.read_csv(fname, sep=';', encoding='utf-8')
    # df_batch = pd.read_csv(fname, sep=';')
    # try:

    with open(fname) as f:
        tweet = json.load(f)
        tweets['statuses'].append(tweet)

    #     df_batch = pd.read_excel(fname, sheetname='Viestit')
    #     print('... aggregating a batch of %s tweets' % (len(df_batch.index)))
    #     # Using the first set of tweets to initialize the dataframe
    #     # if df_all == None:
    #     #     df_all = df_batch.copy()
    #     print(df_batch.columns)
    #     df_all = df_all.append(df_batch)
    # except xlrd.biffh.XLRDError:
    #     print('No tweets found in %s' % fname)


print('Collected a total of %s tweets' % len(tweets['statuses']))

with open('data/tweets-aggregate.json', 'w') as f:
    json.dump(tweets, f, indent=1)

#
# print('Processing and serializing:')
# # print('Serializing %s tweets in CSV' )
# # df_all.to_csv('data/02-aggregate/tweets-full-set.csv', encoding='utf-8')
# # df.to_csv(csv_fname, encoding='utf-8')
# # print('... done')
# print('... removing duplicates')
# df_all['Influencer'] = df_all['kirjoittaja']
# df_all['URL'] = df_all[u'linkki alkuperäiseen']
# df_all.drop_duplicates(subset=['URL'], inplace=True)
# # Most of our analyses use either hashtags or mentioned users:
# print('... extracting hashtags and mentioned users')
# df_all['content'] = df_all[u'tekstisisältö']
# df_all['hashtags'] = df_all.content.apply(hashtags)
# df_all['users_mentioned'] = df_all.content.apply(users_mentioned)
#
# print('... serializing %s unique tweets in CSV' % len(df_all.index))
# df_all.to_csv('data/02-aggregate/tweets-full-set-unique.csv', encoding='utf-8')
# print('... done')
