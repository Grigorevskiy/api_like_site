
from rest_framework.test import APITestCase
from django.test import Client
from django.contrib.auth.models import User


class TestAnonymousOrderApi(APITestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create()

    def test_crete_an_order(self):
        response = self.client.post('/order_anonymous/', data={'name': 'Test User',
                                                               'description': 'desc',
                                                               'duration': 10,
                                                               'email': 'wenbwhj@mail.ru',
                                                               'phone': 21121})

        self.assertEqual(201, response.status_code)

    def test_get_an_order_if_not_admin(self):
        self.client.force_login(self.user)
        response = self.client.get('/order_anonymous/')

        self.assertEqual(403, response.status_code)

    def test_an_orders_if_not_admin(self):
        self.client.force_login(self.user)
        response = self.client.get('/order_anonymous/')

        self.assertEqual(403, response.status_code)
