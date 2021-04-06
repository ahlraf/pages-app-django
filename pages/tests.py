from django.test import TestCase # if we had a database

# Create your tests here.
from django.test import SimpleTestCase # since we're not using a database

class SimpleTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)
