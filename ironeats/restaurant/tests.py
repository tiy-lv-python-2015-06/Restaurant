from django.test import TestCase
from django.test.client import RequestFactory
from restaurant.views import createrest

# Create your tests here.

class CreateRestTest(TestCase):
    """
    Test createrest at url w/ POST
    """
    def setUp(self):
        self.factory = RequestFactory()

    def test_details(self):
        request = self.factory.post('/register/restaurant')

        response = createrest(request)
        self.assertEqual(response.status_code, 200)
