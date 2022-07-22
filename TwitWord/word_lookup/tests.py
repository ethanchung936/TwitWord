from django.test import TestCase
from .tweet_fetch import get_tweets

# Test to see if the home page is working
class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/home/')
        self.assertEquals(response.status_code, 200)
        
    def test_home_page_redirect(self):
        response = self.client.get('/home/test')
        self.assertEquals(response.status_code, 301)
        
# Test get_tweets function
class GetTweetsTest(TestCase):
    def test_get_tweets(self):
        tweets = get_tweets('test')
        self.assertEquals(len(tweets), 5)