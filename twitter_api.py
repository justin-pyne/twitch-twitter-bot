from tweepy import OAuthHandler, API
import config

# Authenticate with Twitter API
def get_twitter_api():
    auth = OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
    auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
    return API(auth)

# Function to send a tweet
def send_tweet(tweet_text):
    twitter_api = get_twitter_api()
    twitter_api.update_status(tweet_text)
