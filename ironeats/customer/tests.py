from django.test import TestCase
from django.test.client import RequestFactory
from customer.views import createuser

# Create your tests here.

class CreateUserTest(TestCase):
    """
    Test createuser at url w/ POST
    """
    def setUp(self):
        self.factory = RequestFactory()

    def test_details(self):
        request = self.factory.post('/register/customer')

        response = createuser(request)
        self.assertEqual(response.status_code, 200)
