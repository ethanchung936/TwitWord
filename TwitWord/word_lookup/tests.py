from django.test import TestCase
from .tweet_fetch import get_tweets, get_ids
from word_lookup.models import WordTable
from random import randint

# Test to see if the pages are working
class WebpageTests(TestCase):
    def setUp(self):
        WordTable.objects.create(word='first test')
    
    def test_home_page_status_code(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)
        
    def test_home_page_redirect(self):
        response = self.client.get('/tweets')
        self.assertEquals(response.status_code, 301)
        
    def test_go_to_correct_uuid_url_no_redirect(self):
        response = self.client.get('/tweets/{}'.format(WordTable.objects.get(word='first test').id))
        self.assertIs(response.status_code, 200)
        
    def test_incorrect_url_301(self):
        response = self.client.get('/{0}'.format(randint(1, 100)))
        self.assertEquals(response.status_code, 301)
        
    def test_incorrect_url_404(self):
        response = self.client.get('/{0}/{0}'.format(randint(1, 100)))
        self.assertEquals(response.status_code, 404)
        
# Test get_tweets function
class TweetFetchTests(TestCase):
    def test_get_tweets_count(self):
        tweets = get_tweets('i')
        self.assertGreaterEqual(len(tweets), 4)
        
    def test_get_ids_type(self):
        tweets = get_tweets('i')
        id_left, id_right = get_ids(tweets)
        self.assertIs(type(id_left[0]), str)
        
    def test_get_ids_length(self):
        tweets = get_tweets('i')
        id_left, id_right = get_ids(tweets)
        self.assertGreaterEqual(len(id_left), len(id_right))
                
# Test WordTable model
class WordTableTestCase(TestCase):
    def setUp(self):
        WordTable.objects.create(word='second test')
        WordTable.objects.create(word='third test')
        
    def test_word_table_different_ids(self):
        second_test = WordTable.objects.get(word='second test')
        first_test = WordTable.objects.get(word='third test')
        self.assertNotEquals(first_test.id, second_test.id)