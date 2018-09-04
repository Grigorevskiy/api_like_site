from rest_framework.test import APITestCase
from django.test import Client
from api.models import Category


class TestCategoryApi(APITestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Test Category")

    def test_get_categories(self):
        response = self.client.get('/category/')
        self.assertEqual(200, response.status_code)

    def test_get_categories_details(self):
        response = self.client.get('/category/{}/'.format(self.category.pk))
        self.assertEqual(200, response.status_code)
