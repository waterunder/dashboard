from django.contrib.auth import get_user_model
from django.test import TestCase


class TestSignUpForm(TestCase):
    username = 'testuser'
    email = 'testuser@email.com'

    def test_signup_page_form(self):
        _ = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
