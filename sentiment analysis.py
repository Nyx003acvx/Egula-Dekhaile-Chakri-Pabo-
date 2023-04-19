import tweepy
from textblob import TextBlob

consumer_key='MxlVgJ2BVLEqnWsMxUsOrUpCH'
consumer_secret='5TtDQsZke2JBjlwz8hE6AVUjyn5JWLVgYBwF8inOxSnXuEbxIe'


access_token = '750245524352229376-pwzITvl6nMRuX1d8GjM0aOPtiRgTU9q'

access_token_secret = 'gOK5UtMLAAHnmVK21TPWW9UI9vf740aOfjNM4HA625GYU'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweet = api.search_tweets('PewDiePie')

for tweet in public_tweet: 
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
