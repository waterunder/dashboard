from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from sellers.models import Seller
from sellers.views import SellerCreate, SellerDetailView, SellerListView


class SellerTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='testpass123',
        )
        self.seller = Seller.objects.create(
            name='Test Company LLC',
            description='Top worldwide experts in selling',
            email='testcompany@email.com',
            address1='Av de Mayo 855, portaldelsur, CABA',
            zip_code='1086',
            city='Buenos Aires',
            country='uk',
            owner=self.user,
        )

    def test_seller_list_view_works_for_loggedin_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('seller_list'))
        no_response = self.client.get('/seller/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.seller.name.title())
        self.assertNotContains(response, 'Hi I should not be on this page!')
        self.assertTemplateUsed(response, 'sellers/seller_list.html')
        self.assertEqual(no_response.status_code, 404)

    def test_seller_list_view_redirects_for_anonymous_user(self):
        response = self.client.get(reverse('seller_list'))
        no_response = self.client.get('/seller/')

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'sellers/seller_list.html')
        self.assertEqual(no_response.status_code, 404)

    def test_seller_list_resolves_sellerlistview(self):
        view = resolve(reverse('seller_list'))
        self.assertEqual(view.func.__name__, SellerListView.as_view().__name__)

    def test_seller_detail_view_works_for_loggedin_user(self):
        self.client.force_login(self.user)
        response = self.client.get(self.seller.get_absolute_url())
        no_response = self.client.get('/sellers/5555')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.seller.name.title())
        self.assertNotContains(response, 'Hi I should not be on this page')
        self.assertTemplateUsed(response, 'sellers/seller_detail.html')
        self.assertEqual(no_response.status_code, 404)

    def test_seller_detail_view_redirects_for_anonymous_user(self):
        response = self.client.get(self.seller.get_absolute_url())
        no_response = self.client.get('/sellers/1243/')

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'sellers/seller_detail.html')
        self.assertEqual(no_response.status_code, 404)

    def test_seller_detail_resolves_sellerdetailview(self):
        view = resolve(self.seller.get_absolute_url())
        self.assertEqual(view.func.__name__, SellerDetailView.as_view().__name__)


class SellerCreateTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='testpass123'
        )

        self.seller = Seller.objects.create(
            name='Test Company LLC',
            description='Top worldwide experts in selling',
            email='testcompany@email.com',
            address1='Av de Mayo 855, portaldelsur, CABA',
            zip_code='1086',
            city='Buenos Aires',
            country='uk',
            owner=self.user,
        )

    def test_seller_create_page_works_for_logged_in_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('seller_create'))
        no_response = self.client.get('/seller/create/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'create')
        self.assertTemplateUsed(response, 'sellers/seller_form.html')
        self.assertNotContains(response, 'Hi I should not be on this page')
        self.assertEqual(no_response.status_code, 404)

    def test_seller_create_page_redirects_for_anonymous_user(self):
        response = self.client.get(reverse('seller_create'))
        no_response = self.client.get('/seller/create/')

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'sellers/seller_form.html')
        self.assertEqual(no_response.status_code, 404)

    def test_seller_create_page_resolve_sellercreate(self):
        view = resolve('/sellers/create/')
        self.assertEqual(view.func.__name__, SellerCreate.as_view().__name__)
