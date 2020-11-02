from IPython import display
import math
from pprint import pprint
import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
import praw
import redditdetails

#tutorial: https://www.learndatasci.com/tutorials/sentiment-analysis-reddit-headlines-pythons-nltk/

reddit = praw.Reddit(client_id=redditdetails.client_id,
                     client_secret=redditdetails.client_secret,
                     user_agent=redditdetails.username)
sns.set(style='darkgrid', context='talk', palette='Dark2')

headlines = set()

for submission in reddit.subreddit('thebachelor').new(limit=None):
    headlines.add(submission.title)
    display.clear_output()
    #print(str(len(headlines)) + " " + submission.title)
    print(len(headlines))
import nltk
nltk.download("vader_lexicon")
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()
results = []

for line in headlines:
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = line
    results.append(pol_score)

pprint(results[:10], width=100)

df = pd.DataFrame.from_records(results)
print(df.head(20))