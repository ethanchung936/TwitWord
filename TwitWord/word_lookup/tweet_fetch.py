import tweepy as tw

# your Twitter API key and API secret
my_api_key = "vhtMACAJiuqAOBHlGtGQkOQzw"
my_api_secret = "Q2f3umR9davc18AmdGYPd0QQbgduDJgN3DUGLwI7QmH0rdoMlw"

# authenticate
auth = tw.OAuth2AppHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

def get_tweets(keyword):
    """Gets a list of 5 tweets based on a keyword

    Args:
        keyword (str): The keyword to search for

    Returns:
        a list of tweet objects
    """
    query = "{} -filter:retweets lang:en".format(keyword)
    tweets = api.search_tweets(query, tweet_mode = 'extended', count = 5)
    return tweets



