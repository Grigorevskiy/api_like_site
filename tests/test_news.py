
from rest_framework.test import APITestCase
from api.models import News
from django.test import Client
from django.contrib.auth.models import User


class TestNewsAPI(APITestCase):

    def setUp(self):
        self.client = Client()
        self.news = News.objects.create(title='Title Of News',
                                        short_description="short description",
                                        body="BODYYY")
        self.news.save()
        self.admin_user = User.objects.create_superuser(email='test@mail.ru', username='test', password='test')

    def test_get_news(self):
        response = self.client.get('/news/')

        self.assertEqual(200, response.status_code)

    def test_get_details_news(self):
        response = self.client.get('/news/{}/'.format(self.news.id))

        self.assertEqual(200, response.status_code)

    def test_create_news_as_admin(self):
        self.client.force_login(self.admin_user)

        create_news = self.client.post('/news/', data={'title': 'new news',
                                                       'short_description': 'des!',
                                                       'body': 'body of new news'})

        self.assertEqual(201, create_news.status_code)
