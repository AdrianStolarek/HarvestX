from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from pandas import DataFrame as df
import json
import time
from lm_module import extract_keywords_and_summary
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def configure_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver

def collect_tweets(query, count=100):
    driver = configure_driver()
    search_url = f"https://x.com/{query}"
    driver.get(search_url)
    time.sleep(3)

    tweets_data = []
    last_height = driver.execute_script("return document.body.scrollHeight")

    while len(tweets_data) < count:
        tweets = driver.find_elements(By.XPATH, '//article[@role="article"]//div[@data-testid="tweetText"]')
        for tweet in tweets:
            try:
                text = tweet.text
                print(text)
                tweets_data.append({'text': text})
                if len(tweets_data) >= count:
                    break
            except Exception as e:
                print("Error while scraping tweet:", e)
                continue

    driver.quit()
    return tweets_data

queries = ["realDonaldTrump", "elonmusk", "ElbridgeColby", "TuckerCarlson", "JDVance"]
all_tweets = []

for query in queries:
    tweets = collect_tweets(query, count=5)
    all_tweets.extend(tweets)

json_data = json.dumps(all_tweets, indent=4)
print(json_data)

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

json_analyzed_data = json.dumps(analyzed_tweets, indent=4)
print(json_analyzed_data)