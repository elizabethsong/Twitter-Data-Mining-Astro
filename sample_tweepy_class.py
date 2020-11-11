import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import GetOldTweets3 as got
import pandas as pd
import json
import csv
import sys
import time
import tokens.py

#reload(sys)
#sys.setdefaultencoding('utf8')

def toDataFrame(tweets):
    # COnvert to data frame
    DataSet = pd.DataFrame()

    DataSet['tweetID'] = [tweet.id for tweet in tweets]
    DataSet['tweetText'] = [tweet.text.encode('utf-8') for tweet in tweets]
    DataSet['userLocation'] = [tweet.user.location for tweet in tweets]
    DataSet['userTimezone'] = [tweet.user.time_zone for tweet in tweets]
    DataSet['Coordinates'] = [tweet.coordinates for tweet in tweets]
    DataSet['GeoEnabled'] = [tweet.user.geo_enabled for tweet in tweets]
    DataSet['tweetRetweetCt'] = [tweet.retweet_count for tweet in tweets]
    DataSet['tweetFavoriteCt'] = [tweet.favorite_count for tweet in tweets]
    DataSet['tweetSource'] = [tweet.source for tweet in tweets]
    DataSet['tweetCreated'] = [tweet.created_at for tweet in tweets]
    DataSet['userID'] = [tweet.user.id for tweet in tweets]
    DataSet['userScreen'] = [tweet.user.screen_name for tweet in tweets]
    DataSet['userName'] = [tweet.user.name for tweet in tweets]
    DataSet['userCreateDt'] = [tweet.user.created_at for tweet in tweets]
    DataSet['userDesc'] = [tweet.user.description for tweet in tweets]
    DataSet['userFollowerCt'] = [tweet.user.followers_count for tweet in tweets]
    DataSet['userFriendsCt'] = [tweet.user.friends_count for tweet in tweets]
    DataSet['Language'] = [tweet.user.lang for tweet in tweets]
    tweets_place= []
    #users_retweeted = []
    for tweet in tweets:
        if tweet.place:
            tweets_place.append(tweet.place.full_name)
        else:
            tweets_place.append('null')
    DataSet['TweetPlace'] = [i for i in tweets_place]
    #DataSet['UserWhoRetweeted'] = [i for i in users_retweeted]

    return DataSet

OAUTH_KEYS = {'consumer_key':tokens.api_key, 'consumer_secret':tokens.api_secret_key,
    'access_token_key':tokens.access_token_key, 'access_token_secret':tokens.access_token_secret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])

api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)
else:
    print ("Scraping data now") # Enter lat and long and radius in Kms  q='ganesh'
    #cursor = tweepy.Cursor(api.search,geocode="23.50000,91.16000,50km",since='2017-09-01',until='2017-09-05',lang='en',count=10000)
    #cursor = tweepy.Cursor(api.search,geocode="43.17305,-77.62479,50km",since='2017-09-01',until='2017-09-05',lang='en',count=10000)
    cursor = tweepy.Cursor(api.search, q="#aries",count=1000,lang="en")
    
    results=[]
    for item in cursor.items(1000): # Remove the limit to 1000
        results.append(item)
    #results2 = re.sub(r'https?://.*?', '', results)
    
    #results3 = re.sub(r'@.*? ', '', results2)
    


    DataSet = toDataFrame(results)
    DataSet.to_csv('aries.csv',index=False)
    print ("Completed.. !!")