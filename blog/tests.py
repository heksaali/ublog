from http import HTTPStatus
from django.test import TestCase
from django.contrib.auth import get_user_model


class TestNewPostLogin(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_posting_form(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/new-post/')
        self.assertEqual(response.status_code, HTTPStataus.OK)