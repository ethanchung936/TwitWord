import tweepy as tw
import requests

# Twitter API key and API secret
my_api_key = "vhtMACAJiuqAOBHlGtGQkOQzw"
my_api_secret = "Q2f3umR9davc18AmdGYPd0QQbgduDJgN3DUGLwI7QmH0rdoMlw"

# authenticate
auth = tw.OAuth2AppHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)


def get_tweets(keyword):
    '''Gets a list of 4 tweets based on a keyword

    Args:
        keyword (str): The keyword to search for

    Returns:
        a list of tweet objects
    '''
    query = '"{}" -filter:retweets -filter:replies lang:en'.format(keyword)
    tweets = api.search_tweets(query, count = 10)
    return tweets

def get_ids(tweets):
    '''Get two lists of tweet embedded tweets from a list of tweets

    Args:
        tweets (list): A list of tweet objects

    Returns:
        left_tweets and right_tweets (list): lists of embedded tweets
    '''
    left_tweets = []
    right_tweets = []
    i = 0
    for tweet in tweets:
        if i <= 5:
            twt_http = requests.get('https://publish.twitter.com/oembed?url=https://twitter.com/twitter/status/' + tweet.id_str + '&dnt=false&maxwidth=180&maxheight=200')
            twtjson = twt_http.json()
            emb_tweet = twtjson.get('html')
            # sort into two lists
            if i % 2 == 0:
                left_tweets.append(emb_tweet)
            elif i % 2 == 1:
                right_tweets.append(emb_tweet)
            i += 1
    return left_tweets, right_tweets