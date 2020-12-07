#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
import os
from os import environ
import random
import numpy as np

argfile = str(sys.argv[1])

# CONSUMER_KEY = environ['CONSUMER_KEY']
# CONSUMER_SECRET = environ['CONSUMER_SECRET']
# ACCESS_KEY = environ['ACCESS_KEY']
# ACCESS_SECRET = environ['ACCESS_SECRET']
CONSUMER_KEY = "0JezAgKPgQVBhYLjDdoUntX7q"
CONSUMER_SECRET = "EWS6I2W2Kzkm8M1vmdZo0hiAyhYxrN3Gg8BQSoAmdrUAKNNuaJ"
ACCESS_KEY = "1336048738146660354-dYdYBguqkxWDJiS4XCoaCuPxgfrFQc"
ACCESS_SECRET = "PjU6rhYk2bQHlBrXZePDIib2WpoUR6TrUIThiG4GV1FgC"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.read()
filename.close()

split_text = f.split("\n====================\n")

valid_text = [x for x in split_text if len(x) <= 280]

tweet = np.random.choice(valid_text, 1)
api.update_status(tweet[0])
#for line in f:
 #   api.update_status(line)
  #  time.sleep(3600)
