import snscrape.modules.twitter as sntwitter
import csv
maxTweets = 150

csvFile = open('gemini.csv', 'a', newline='', encoding='utf8')

csvWriter = csv.writer(csvFile)
csvWriter.writerow(['text'])

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:@GeminiTerms + since:2015-12-02 until:2020-11-10-filter:replies').get_items()):
    if i > maxTweets :
        break
    if tweet.likeCount > 100:
        csvWriter.writerow([tweet.content])
csvFile.close()