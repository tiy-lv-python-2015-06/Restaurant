from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here.
from restaurant.models import Restaurant, FoodItem


class RestaurantMethodTest(TestCase):

    def test_has_no_menu(self):
        user = User(username='test', email='test@test.com', password='test')
        user.save()
        rest = Restaurant(business_name="I love donuts", email='test@test.com',
                          address='1122 City Center', city='LV', state='NV',
                          zip_code='89178', phone_number='555-1212', user=user)
        rest.save()
        self.assertFalse(rest.has_menu(), "No Menu")

    def test_has_menu(self):
        user = User(username='test', email='test@test.com', password='test')
        user.save()
        rest = Restaurant(business_name="I love donuts", email='test@test.com',
                          address='1122 City Center', city='LV', state='NV',
                          zip_code='89178', phone_number='555-1212', user=user)
        rest.save()
        menu = FoodItem(restaurant=rest, name='Sprinkle Donut',
                        price='2.99', description='your favorite sprinkle donut',
                        category='D')
        menu.save()
        self.assertTrue(rest.has_menu(), "Yes, there's a Menu")

    # def test_get_no_menu_items(self):
    #     user = User(username='test', email='test@test.com', password='test')
    #     user.save()
    #     rest = Restaurant(business_name="I love donuts", email='test@test.com',
    #                       address='1122 City Center', city='LV', state='NV',
    #                       zip_code='89178', phone_number='555-1212', user=user)
    #     rest.save()
    #     self.assertFalse(rest.get_menu_items(), "There are no menu items yet.")


class RestaurantVewTests(TestCase):

    def test_restaurant_profile_404(self):
        url = reverse('restaurant_profile', args=[100])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    # def test_create_menu_return_new_menu(self):
    #     test_user = User.objects.create_user('test', 'test@test.com', 'pass')
    #     test_user.save()
    #
    #     rest = Restaurant(business_name="I love donuts", email='test@test.com',
    #                       address='1122 City Center', city='LV', state='NV',
    #                       zip_code='89178', phone_number='555-1212',
    #                       user=test_user)
    #     rest.save()
    #     fooditem = FoodItem(restaurant=rest, name='Sprinkle Donut',
    #                         price='2.99',
    #                         description='your favorite sprinkle donut',
    #                         category='D')
    #     fooditem.save()
    #
    #     response = self.client.get(reverse('manage_menu', args=[rest.id]))
    #     self.assertContains(response, "Testing")

    def test_order_list_404(self):
        url = reverse('order_list', args=[100])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_create_menu_404(self):
        url = reverse('create_menu', args=[100])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 201)
