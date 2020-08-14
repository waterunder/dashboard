from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from sellers.models import Seller
from sellers.views import SellerCreate


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

    def test_seller_listing(self):
        self.assertEqual(f'{self.seller.name}', 'Test Company LLC')
        self.assertEqual(f'{self.seller.description}', 'Top worldwide experts in selling')
        self.assertEqual(f'{self.seller.email}', 'testcompany@email.com')
        self.assertEqual(f'{self.seller.address1}', 'Av de Mayo 855, portaldelsur, CABA')
        self.assertEqual(f'{self.seller.zip_code}', '1086')
        self.assertEqual(f'{self.seller.city}', 'Buenos Aires')
        self.assertEqual(f'{self.seller.country}', 'uk')

    def test_seller_list_view_works_for_loggedin_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('seller_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.seller.name.title())
        self.assertNotContains(response, 'Hi I should not be on this page!')
        self.assertTemplateUsed(response, 'sellers/seller_list.html')

    def test_seller_detail_view_works_for_loggedin_user(self):
        self.client.force_login(self.user)
        response = self.client.get(self.seller.get_absolute_url())
        no_response = self.client.get('/sellers/5555')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.seller.name.title())
        self.assertNotContains(response, 'Hi I should not be on this page')
        self.assertTemplateUsed(response, 'sellers/seller_detail.html')

        self.assertEqual(no_response.status_code, 404)


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
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'create')
        self.assertTemplateUsed(response, 'sellers/seller_form.html')
        self.assertNotContains(response, 'Hi I should not be on this page')

    def test_seller_create_page_redirects_for_anonymous_user(self):
        response = self.client.get(reverse('seller_create'))
        self.assertEqual(response.status_code, 302)
        self.assertContains(response, 'login')
        self.assertTemplateUsed(response, 'account/login.html')
        self.assertNotContains(response, 'Hi I should not be on this page')
        self.assertNotContains(response, 'Create')

    def test_seller_create_page_resolve_sellercreate(self):
        view = resolve('/sellers/create/')
        self.assertEqual(view.func.__name__, SellerCreate.as_view().__name__)
