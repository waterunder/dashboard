from django.test import TestCase
from django.urls import resolve, reverse

from pages import forms
from pages.views import AboutPageView, ContactUsView, HomePageView


class HomePageTests(TestCase):
    def test_homepage_works(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Homepage')
        self.assertNotContains(response, 'Hi there! I should not be here')

    def test_home_page_resolves_homepageview(self):
        view = resolve('/pages/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(TestCase):
    def test_aboutpage_works(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertContains(response, 'About')
        self.assertNotContains(response, 'Hi I should be on this page!')

    def test_about_page_resolves_aboutpageview(self):
        view = resolve('/pages/about/')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)


class ContactPageTests(TestCase):
    def test_contact_us_page_works(self):
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_form.html')
        self.assertContains(response, 'Contact Us')
        self.assertNotContains(response, 'Hi I should not be on this page')
        self.assertIsInstance(response.context['form'], forms.ContactForm)

    def test_contact_us_page_resolve_contactpageview(self):
        view = resolve('/pages/contact-us/')
        self.assertEqual(view.func.__name__, ContactUsView.as_view().__name__)
