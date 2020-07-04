from django.test import TestCase
from django.urls import resolve, reverse

from .views import AboutPageView, HomePageView


class HomePageTests(TestCase):
    def test_homepage_works(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Homepage')
        self.assertNotContains(response, 'Hi there! I should not be here')

    def test_home_page_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(TestCase):
    def test_aboutpage_works(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertContains(response, 'About')
        self.assertNotContains(response, 'Hi I should be on this page!')

    def test_about_page_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
