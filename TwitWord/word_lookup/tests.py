from django.test import TestCase

# Create your tests here.

# Test to see if the home page is working
class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/home/')
        self.assertEquals(response.status_code, 200)
