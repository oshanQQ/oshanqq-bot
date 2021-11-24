import os
import tweepy
from dotenv import load_dotenv


def twitter_api():
    load_dotenv()
    API_KEY = os.environ.get("API_KEY")
    API_KEY_SECRET = os.environ.get("API_KEY_SECRET")
    ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    return api


def get_user_tweets():
    user_info = twitter_api().user_timeline(user_id="oshanqq", count=30)
    user_tweets = ""

    for tweet in user_info:
        user_tweets += tweet.text

    return user_tweets
