# Horoscope Project: Data Mining

To run, there are 3 main files:
1. **Testastroold.py** retrieves old tweets, up to maxTweets. It uses snscrape (previously GetOldTweets3, which is no longer up to date with the current version of Twitter) and retrieves tweets from different astrological Twitter accounts. 
We chose Twitter accounts based on popular and recent accounts that have been tweeted and followed by many other users. Tweets are only filtered to the csv file if there are more than 100 likes (meaning it is legitimate, not spammy tweets, and other people like the content).
2. **Exploratory_data_analysis1.py** is how we used stemming, lemmatization, tokenization, removed stopwords, hashtags, links, etc. to preprocess the tweets. This would make results of Bertmoticon more accurate. Our preprocessed and cleaned tweets were updated in the same csv file.
3. **Astro-emojis.py** is the last file to run. It runs Bertmoticon and infers emojis given the updated csv file generated from Part 2. It takes a hashmap and generates total probabilities of all emojis. (Note: laughing face emoji somehow is inferred in every tweet, despite the horoscope so this was often ignored).

We scraped over a thousand tweets on the horoscope (Cancer, Leo, Aries, Taurus, etc.) and contrasted the results from Bertmoticon to see which emojis aligned the most with certain horoscope's Twitter accounts. 


