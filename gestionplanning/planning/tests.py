from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from models import *
from django.contrib import auth


# Create your tests here.


class IndexPageTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_page_connected(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
