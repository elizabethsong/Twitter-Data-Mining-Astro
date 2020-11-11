# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import nltk 
from nltk.corpus import stopwords
import string
import re
#import emoji
from nltk.stem.snowball import SnowballStemmer
import tweepy
#import botometer
import csv
import pandas as pd
import tokens
pd.set_option('display.max_colwidth', 100)

#FOR THE BOTOMETER
rapidapi_key = "3e780f0aa5msh2c957bc129c5c4fp1e42aajsn52ac7cb58a9d" # now it's called rapidapi key
OAUTH_KEYS = {'consumer_key':tokens.api_key, 'consumer_secret':tokens.api_secret_key,
    'access_token_key':tokens.access_token_key, 'access_token_secret':access_token_secret}

"""
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **OAUTH_KEYS)
"""

"""
def remove_emoji(text):
    """"""Converts emojis to words
    """"""
    #text  = "".join([char for char in text if char in emoji.UNICODE_EMOJI])
    text = emoji.demojize(text)
    return text
"""

def tokenization(text):
    text = re.split('\W+', text)
    return text

def remove_stopwords(text):
    """Removes stopwords
    Makes sure to tokenize / put all words in list
    """
    stop_words = set(stopwords.words("english"))
    text = tokenization(text)
    filtered_tweet = [w for w in text if not w in stop_words] 
    return filtered_tweet

def stemming(text):
    """Assumes that text has already been tokenized
    """
    sb = SnowballStemmer("english")
    for word in text:
        print(word, " : ", sb.stem(word)) 

def remove_url(text):
    pattern = r"http\S+"
    #text = "https://www.google.com"
    text = re.sub(pattern, "",text)
    pattern2 = r"www\S+"
    return re.sub(pattern2, "",text)

def remove_hashtag(text):
    pattern = r"#+"
    return re.sub(pattern, "",text)

def remove_username(text):
    pattern = r"@\S+"
    return re.sub(pattern, "",text)

def remove_spam(text):
    #pattern = r"\xe\x\m+"
    pattern = r'b"+'   
    text = re.sub(pattern, "",text)
    pattern = r"b'+"
    return re.sub(pattern, "",text)

def remove_spam2(text):
    pattern = r"&amp"
    return re.sub(pattern, "",text)

def remove_retweet(text):
    pattern = r"RT+"
    return re.sub(pattern, "",text)

def remove_number(text):
    return ''.join([i for i in text if not i.isdigit()])


"""
def checkBot(author):
    """"""Input can be @username or author ID
    """"""
    #try:
    currID = author
    result = bom.check_account(currID)
    check = result['scores']
    if check['english'] > 0.55:
        return 1 #is a Bot
    else:
        return 0
    #except tweepy.error.TweepError:
        #pass
"""

tweet_df = pd.read_csv("gemini.csv")
df  = pd.DataFrame(tweet_df[['text']])
#df['text'] = df['text'].apply(lambda x: remove_emoji(x))
df['text'] = df['text'].apply(lambda x: remove_hashtag(x))
df['text'] = df['text'].apply(lambda x: remove_url(x))
df['text'] = df['text'].apply(lambda x: remove_username(x))
df['text'] = df['text'].apply(lambda x: remove_number(x))
df['text'] = df['text'].apply(lambda x: remove_spam(x))
df['text'] = df['text'].apply(lambda x: remove_spam2(x))
df['text'] = df['text'].apply(lambda x: remove_retweet(x))
df['text'] = df['text'].apply(lambda x: remove_retweet(x))
df[~df['text'].str.contains("today")]

#df['bot?'] = df['id'].apply(lambda x: checkBot(x))
#df['text'] = df['text'].apply(lambda x: remove_stopwords(x))
#df['text'] = df['text'].apply(lambda x: tokenization(x))
print(df.head(10))
df.to_csv("gemini.csv")


 
"""

tweet="Testing🤠 Sarah's @what cradle loves pizza and cats but she doesn't herself. #lol https://google.com www.cya.com"
tweet = remove_emoji(tweet)
tweet = remove_url(tweet)
tweet = remove_hashtag(tweet)
tweet = remove_username(tweet)
print(tweet)
print(tokenization(tweet))
tweet = remove_stopwords(tweet)
print(stemming(tweet))
"""
