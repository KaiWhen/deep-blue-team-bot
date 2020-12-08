#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
import os
from os import environ
import random
import numpy as np

argfile = str(sys.argv[1])

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile, 'r')
f=filename.read()
filename.close()

split_text = f.split("\n====================\n")

valid_text = [x for x in split_text if len(x) <= 280]

for x in range(5):
    tweet = np.random.choice(valid_text, 1)
    api.update_status(tweet[0])
    time.sleep(600)
#for line in f:
 #   api.update_status(line)
  #  time.sleep(3600)
