from tokens import keys

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_secret = keys['access_secret']

searchterm = 'popular thing'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class Listener(StreamListener):
 
  def on_data(self, data):
    try:
      filename = searchterm + '.json'
      with open(filename, 'a+') as f:
        f.write(data)
        return True
    except BaseException as e:
        print("FAILED TO WRITE DATA: %s" % str(e))
    return False

  def on_error(self, status):
    print(status)
    if status == 420:
      return False
    return True

  def on_status(self, status):
    print(status)

stream = Stream(auth, Listener())
stream.filter(track=[searchterm], async=True)