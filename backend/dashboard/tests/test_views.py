from django.test import TestCase
from django.urls import resolve, reverse

from dashboard.views import DashboardPageView, ProfilePageView


class DashboardPageTests(TestCase):
    def test_dashboard_page_works(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/index.html')
        self.assertContains(response, 'Dashboard')
        self.assertNotContains(response, 'Hi there! I should not be here')

    def test_dashboard_page_resolves_dashboardpageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, DashboardPageView.as_view().__name__)


class ProfilePageTests(TestCase):
    def test_dashboard_profile_page_works(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/profile.html')
        self.assertContains(response, 'Profile')
        self.assertNotContains(response, 'Hi there! I should not be here')

    def test_dashboard_profile_resolves_dashboardprofileview(self):
        view = resolve('/profile/')
        self.assertEqual(view.func.__name__, ProfilePageView.as_view().__name__)
