from rest_framework.test import APITestCase
from django.test import Client
from api.models import Category, Journey
from django.contrib.auth.models import User


class TestCategoryApi(APITestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create()
        category = Category.objects.create(name="Test Category")
        self.journey = Journey.objects.create(category=category, title="Test Journey", description="Description",
                                              durations_days=10, durations_night=11, price=1000, )
        self.journey.save()

    def test_get_comments_if_authorized(self):
        self.client.force_login(self.user)
        response = self.client.get('/journey/{}/comments/'.format(self.journey.id))

        # assert a 200 status code was returned
        self.assertEqual(200, response.status_code)

    def test_get_comments_if_unauthorized(self):
        response = self.client.get('/journey/{}/comments/'.format(self.journey.id))

        # assert a 200 status code was returned
        self.assertEqual(200, response.status_code)

    def test_add_new_comment_if_unauthorized(self):
        response = self.client.post('/journey/{}/comments/create/'.format(self.journey.id),
                                                        data={'body': 'This is auto test'})

        # assert a 401 status code was returned
        self.assertEqual(401, response.status_code)

    def test_add_new_comment_if_authorized(self):
        expected_text = 'This is auto test'
        self.client.force_login(self.user)
        response = self.client.post('/journey/{}/comments/create/'.format(self.journey.id),
                                                                data={'body': expected_text,
                                                                      'journey': self.journey.id,
                                                                      'user': self.user.id})

        print(response.data)
        # assert a 201 status code was returned
        self.assertEqual(201, response.status_code)
        self.assertEqual(expected_text, response.data['body'])
        self.assertEqual(self.user.id, response.data['user'])
