from django.test import TestCase
from django.urls import resolve, reverse

from users.views import SignupPageView


class SignUpPageTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_page_works(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'SIGN UP')
        self.assertNotContains(self.response, 'Hi there. I should not be here')

    def test_signup_page_resolves_signuppageview(self):
        view = resolve('/users/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
