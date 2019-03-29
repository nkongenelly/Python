# To run this code, first edit config.py with your configuration, then:
#
# mkdir data
# python twitter_stream_download.py -q apple -d data
# 
# It will produce the list of tweets for the query "apple" 
# in the file data/stream_apple.json

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import config
import json
import MySQLdb

#        replace mysql.server with "localhost" if you are running via your own server!
#                        server       MySQL username	MySQL pass  Database name.
conn = MySQLdb.connect("localhost","root","","pythontweets")

c = conn.cursor()

conn.set_character_set('utf8')
c.execute('SET NAMES utf8;')
c.execute('SET CHARACTER SET utf8;')
c.execute('SET character_set_connection=utf8;')

""" A listener handles tweets that are received from the stream.
This is a basic listener that just prints received tweets to stdout.

def on_data(self, data):
    print(data)
    return True


"""


class listener(StreamListener):
 

    def on_data(self, data):
        
        all_data = json.loads(data)
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]

        #print((username,tweet))

        c.execute("INSERT INTO tweets (time, username, tweet) VALUES (%s,%s,%s)",
            (datetime.fromtimestamp(time.time()).strftime("%A, %B %d, %Y %I:%M:%S"),username, tweet))

        conn.commit()

        print((username,tweet))

        return True


    def on_error(self, status):
            print(status)

if __name__ == '__main__':
    #l = StdOutListener()
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)

    stream = Stream(auth, listener())
    stream.filter(track=['is','today','new'])
