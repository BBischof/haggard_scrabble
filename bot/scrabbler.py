#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
from parser import haggard_parser as hp
#from our keys module (keys.py), import the keys dictionary
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

mostrecenttweet = api.user_timeline('haggardhawks')[0]

words = hp.reader(mostrecenttweet.text)
scores = hp.scrabble_scores(words)
new_status = hp.write_reply(words, scores)

if new_status:
  api.update_status(new_status, mostrecenttweet.id)

#HH id: 2239350253
