
import json
from rest_framework.test import APITestCase
from django.test import Client
from django.contrib.auth.models import User
from api.models import OrderAnonymous


class TestAnonymousOrderApi(APITestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create()
        self.admin_user = User.objects.create_superuser(email='test@mail.ru', username='test', password='test')
        self.an_order = OrderAnonymous.objects.create(name="Test An Order", description="Des",
                                                      person=10, duration=10, email="ekfnjwe@mail.ru",
                                                      phone=21313)

    def test_crete_an_order(self):
        response = self.client.post('/order_anonymous/create/', data={'name': 'Test User',
                                                                      'description': 'desc',
                                                                      'person': 11,
                                                                      'duration': 10,
                                                                      'email': 'wenbwhj@mail.ru',
                                                                      'phone': 21121})

        self.assertEqual(201, response.status_code)

    def test_update_an_order_as_admin(self):
        self.client.force_login(self.admin_user)

        update_order = self.client.put('/order_anonymous/{}/'.format(self.an_order.id),
                                       data=json.dumps({'name': 'Test User',
                                                        'description': 'desc',
                                                        'person': 11,
                                                        'duration': 10,
                                                        'email': 'wenbwhj@mail.ru',
                                                        'phone': 21121}),
                                       content_type='application/json')

        self.assertEqual(200, update_order.status_code)

    def test_delete_an_order_as_admin(self):
        self.client.force_login(self.admin_user)

        delete_order = self.client.delete('/order_anonymous/{}/'.format(self.an_order.id))

        self.assertEqual(204, delete_order.status_code)

    def test_get_an_order_if_not_admin(self):
        self.client.force_login(self.user)
        response = self.client.get('/order_anonymous/')

        self.assertEqual(403, response.status_code)

    def test_get_list_an_order_if_not_admin(self):
        self.client.force_login(self.user)
        response = self.client.get('/order_anonymous/{}/'.format(self.an_order.id))

        self.assertEqual(403, response.status_code)
