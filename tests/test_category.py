
import json

from rest_framework.test import APITestCase
from django.test import Client
from api.models import Category
from django.contrib.auth.models import User


class TestCategoryApi(APITestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create()
        self.category = Category.objects.create(name="Test Category",
                                                description="Des")

    def test_get_categories(self):
        response = self.client.get('/category/')
        self.assertEqual(200, response.status_code)

    def test_get_category_details(self):
        response = self.client.get('/category/{}/'.format(self.category.pk))
        self.assertEqual(200, response.status_code)

    def test_create_category_as_admin(self):
        user = User.objects.create_superuser(email='test@mail.ru', username='test', password='test')
        self.client.force_login(user)
        response = self.client.post('/category/', data={'name': 'Title',
                                                                'description': 'Description'})
        self.assertEqual(201, response.status_code)

    def test_create_category_as_not_admin(self):
        self.client.force_login(self.user)
        response = self.client.post('/category/', data={'name': 'Title',
                                                                'description': 'Description'})

        # assert a 201 status code was returned
        self.assertEqual(403, response.status_code)

    def test_update_category_as_admin(self):
        user = User.objects.create_superuser(email='test@mail.ru', username='test', password='test')
        self.client.force_login(user)

        update_category = self.client.put('/category/{}/'.format(self.category.pk),
                                          data=json.dumps({'name': 'new name1',
                                                           'description': 'new des'}), content_type='application/json')
        self.assertEqual(200, update_category.status_code)

    def test_update_category_as_not_admin(self):
        update_category = self.client.put('/category/{}/'.format(self.category.pk),
                                          data=json.dumps({'name': 'new name1',
                                                           'description': 'new des'}), content_type='application/json')

        self.assertEqual(401, update_category.status_code)

    def test_delete_category(self):
        self.test_create_category_as_admin()

        delete_category = self.client.delete('/category/{}/'.format(self.category.pk))
        self.assertEqual(204, delete_category.status_code)

        delete_category = self.client.delete('/category/{}/'.format(self.category.pk))
        self.assertEqual(404, delete_category.status_code)

    def test_delete_category_as_not_admin(self):
        delete_category = self.client.delete('/category/{}/'.format(self.category.pk))
        self.assertEqual(401, delete_category.status_code)
