import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'Loy2EJVTB0G0eGjJEO3aTCODJ'
consumer_secret = 'vHx40p0IktFfZr0fJKJt0pvkrJPN7CYmQjviYblJms3mxIiz1K'
access_token = '923908720249229313-np5cLiRK66owI4PtU7FoYLR20KSu62u'
access_secret = 'QRdvChPGJ6em9tPkBJa0eTC34f78Z4xwMZrLAgQ91vTL8'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)