from django.test import TestCase
from django.urls import resolve, reverse

from .views import DashboardPageView


class DashboardPageTests(TestCase):
    def test_dashboard_page_works(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/index.html')
        self.assertContains(response, 'Dashboard')
        self.assertNotContains(response, 'Hi there! I should not be here')

    def test_dashboard_page_resolves_dashboardpageview(self):
        view = resolve('/dashboard/')
        self.assertEqual(view.func.__name__, DashboardPageView.as_view().__name__)
