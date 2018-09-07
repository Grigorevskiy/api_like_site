
import json

from rest_framework.test import APITestCase
from django.test import Client
from api.models import Category, Journey, Comment
from django.contrib.auth.models import User


class TestCategoryApi(APITestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create()
        self.category = Category.objects.create(name="Test Category", description="Des")
        self.journey = Journey.objects.create(category=self.category, title="Test Journey", description="Description",
                                              durations_days=10, durations_night=11, price=1000)
        self.journey.save()

        self.comment = Comment.objects.create(body="Comment body", journey=self.journey, user=self.user)
        self.comment.save()

    def test_get_comments_if_authorized(self):
        self.client.force_login(self.user)
        response = self.client.get('/journey/{}/comments/'.format(self.journey.id))

        self.assertEqual(200, response.status_code)

    def test_get_comments_if_unauthorized(self):
        response = self.client.get('/journey/{}/comments/'.format(self.journey.id))

        self.assertEqual(200, response.status_code)

    def test_create_comment_if_authorized(self):
        expected_text = 'This is auto test'
        self.client.force_login(self.user)
        response = self.client.post('/journey/{}/comments/'.format(self.journey.id),
                                    data={'body': expected_text, 'journey': self.journey.id})

        self.assertEqual(201, response.status_code)
        self.assertEqual(expected_text, response.data['body'])
        self.assertEqual(self.user.id, response.data['user'])

    def test_create_comment_if_unauthorized(self):
        response = self.client.post('/journey/{}/comments/'.format(self.journey.id),
                                    data={'body': 'This is auto test'})

        self.assertEqual(401, response.status_code)

    def test_delete_comment_if_authorized(self):
        self.client.force_login(self.user)
        response = self.client.delete('/journey/{}/comments/{}/'.format(self.journey.id, self.comment.id))

        self.assertEqual(204, response.status_code)

    def test_delete_comment_if_unauthorized(self):
        response = self.client.delete('/journey/{}/comments/{}/'.format(self.journey.id, self.comment.id))

        self.assertEqual(401, response.status_code)

    def test_delete_comment_if_not_owner(self):
        self.test_create_comment_if_authorized()
        comment_id = self.journey.comments.first().id

        another_user = User.objects.create(username='another_user')
        self.client.force_login(another_user)

        delete_comment = self.client.delete('/journey/{}/comments/{}/'.format(self.journey.id, comment_id))

        self.assertEqual(403, delete_comment.status_code)

    def test_update_comment_if_authorized(self):
        self.test_create_comment_if_authorized()
        comment_id = self.journey.comments.first().id

        updated_comment = self.client.put('/journey/{}/comments/{}/'.format(self.journey.id,
                                                                            comment_id),
                                          data=json.dumps({'body': 'Updated Comment', 'journey': self.journey.id}),
                                          content_type='application/json')

        self.assertEqual(200, updated_comment.status_code)

        current_comment = self.client.get('/journey/{}/comments/{}/'.format(self.journey.id, comment_id))

        self.assertEqual(200, current_comment.status_code)
        self.assertEqual(updated_comment.data, current_comment.data)

    def test_update_comment_if_unauthorized(self):
        update_comment = self.client.put('/journey/{}/comments/{}/'.format(self.journey.id,
                                                                           self.journey.comments.first().id),
                                         data=json.dumps({'body': 'Test Update Comment'}),
                                         content_type='application/json')

        self.assertEqual(401, update_comment.status_code)

    def test_update_comment_if_not_owner(self):
        self.test_create_comment_if_authorized()
        comment_id = self.journey.comments.first().id

        another_user = User.objects.create(username="another_user")
        self.client.force_login(another_user)

        update_comment = self.client.put('/journey/{}/comments/{}/'.format(self.journey.id, comment_id))

        self.assertEqual(403, update_comment.status_code)
