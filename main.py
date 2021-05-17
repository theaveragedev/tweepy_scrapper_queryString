import json
import tweepy
import csv

# Read the secret.json to get the credentials
with open('secret.json') as f:
  data = json.load(f)

# Authenticate 
auth = tweepy.OAuthHandler(consumer_key=data['api_key'] , consumer_secret=data['api_secret_key'])
api = tweepy.API(auth, wait_on_rate_limit=True)

# Open/create a file to append data to
csvFile = open('output/result.csv', 'a', newline="")

#Use csv writer
csvWriter = csv.writer(csvFile)

# Query Params
queryString = "oxygen needed urgent exclude:retweets exclude:replies"
limits = 20


# Send query and write to CSV
for tweet in tweepy.Cursor(api.search, q=queryString, lang="en", result_type = "recent").items(limits):
    csvWriter.writerow([tweet.created_at, tweet.user.name.encode('utf-8'), tweet.user.screen_name.encode('utf-8'), tweet.text.encode('utf-8')])

# Close the file
csvFile.close()