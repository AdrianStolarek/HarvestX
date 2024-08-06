from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
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

#def collect_tweets(query, count=100):
#    driver = configure_driver()
#    search_url = f"https://x.com/{query}"
#    driver.get(search_url)
#    time.sleep(3)
#
#    tweets_data = []
#    last_height = driver.execute_script("return document.body.scrollHeight")
#
#    while len(tweets_data) < count:
#        tweets = driver.find_elements(By.XPATH, '//article[@data-testid="tweet"]')
#        for tweet in tweets:
#            try:
#                user = tweet.find_element(By.XPATH, './/span').text
#                text = tweet.find_element(By.XPATH, './/div[2]/div[2]/div[1]').text
#                created_at = tweet.find_element(By.XPATH, './/time').get_attribute('datetime')
#                retweet_count = tweet.find_element(By.XPATH, './/div[@data-testid="retweet"]').text
#                favorite_count = tweet.find_element(By.XPATH, './/div[@data-testid="like"]').text
#
#                tweet_info = {
#                    'user': user,
#                    'text': text,
#                    'created_at': created_at,
#                    'retweet_count': int(retweet_count) if retweet_count else 0,
#                    'favorite_count': int(favorite_count) if favorite_count else 0
#                }
#                tweets_data.append(tweet_info)
#
#                if len(tweets_data) >= count:
#                    break
#            except Exception as e:
#                print("Error while scraping tweet:", e)
#                continue
#
#        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#        time.sleep(3)
#        new_height = driver.execute_script("return document.body.scrollHeight")
#        if new_height == last_height:
#            break
#        last_height = new_height
#
#    driver.quit()
#    return tweets_data

def collect_tweets(query, count=100):
    driver = configure_driver()
    search_url = f"https://x.com/{query}"
    driver.get(search_url)
    time.sleep(3)

    tweets_data = []
    last_height = driver.execute_script("return document.body.scrollHeight")

    while len(tweets_data) < count:
        tweets = driver.find_elements(By.XPATH, '//*[@id="id__k4jrnoy69fd"]')
        for tweet in tweets:
            try:
                print(tweet)
                tweets_data.append(tweet)
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