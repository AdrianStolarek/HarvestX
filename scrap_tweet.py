from bs4 import BeautifulSoup as bs
import requests as req
import json
import tweepy
from lm_module import extract_keywords_and_summary

API_KEY = 'YOUR_API_KEY'
API_SECRET_KEY = 'YOUR_API_SECRET_KEY'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def collect_tweets(query, count=100):
    tweets_data = []
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(count):
        tweet_info = {
            'user': tweet.user.screen_name,
            'text': tweet.full_text,
            'created_at': tweet.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'retweet_count': tweet.retweet_count,
            'favorite_count': tweet.favorite_count
        }
        tweets_data.append(tweet_info)
    return tweets_data

queries = ["#Python", "#DataScience", "#MachineLearning"]
all_tweets = []

for query in queries:
    tweets = collect_tweets(query, count=100)
    all_tweets.extend(tweets)

with open('tweets.json', 'w') as json_file:
    json.dump(all_tweets, json_file, indent=4)

analyzed_tweets = []
for tweet in all_tweets:
    keywords, summary = extract_keywords_and_summary(tweet["text"])
    analyzed_tweet = {
        "user": tweet["user"],
        "text": tweet["text"],
        "keywords": keywords,
        "summary": summary
    }
    analyzed_tweets.append(analyzed_tweet)

with open('analyzed_tweets.json', 'w') as file:
    json.dump(analyzed_tweets, file, indent=4)