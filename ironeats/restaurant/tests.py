from django.test import TestCase

# Create your tests here.
from restaurant.models import Restaurant


class RestaurantTestCase(TestCase):

    def createRest(self):
        Restaurant.objects.create(business_name= 'testrest',
                                  email= 'test@test.com',
                                  address= '11 Test Cir',
                                  city= 'Test Vegas',
                                  state= 'NV',
                                  zip_code= '89104',)

    # def testRestAttrs(self):
    #     testrest = Restaurant.objects.get(business_name= 'testrest')
