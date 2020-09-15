from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import resolve, reverse

from sellers.factories import SellerFactory, UserFactory
from sellers.models import Seller
from sellers.views import (
    SellerCreate,
    SellerDelete,
    SellerDetailView,
    SellerListView,
    SellerUpdate,
)


class SellerListTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.seller = SellerFactory(owner=self.user)

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


class SellerDetailTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.seller = SellerFactory(owner=self.user)

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
        no_response = self.client.get('/sellers/1234/')

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'sellers/seller_detail.html')
        self.assertEqual(no_response.status_code, 404)

    def test_seller_detail_resolves_sellerdetailview(self):
        view = resolve(self.seller.get_absolute_url())
        self.assertEqual(view.func.__name__, SellerDetailView.as_view().__name__)


class SellerCreateTests(TestCase):
    def setUp(self):
        self.user = UserFactory()

        self.seller = SellerFactory(owner=self.user)

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


class SellerUpdateTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.seller = SellerFactory(owner=self.user)

    def test_seller_update_page_works_for_logged_in_user(self):
        self.client.force_login(self.user)
        response = self.client.get(self.seller.get_update_url())
        no_response = self.client.get('/sellers/1234/update/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sellers/seller_update_form.html')
        self.assertContains(response, 'Update')
        self.assertNotContains(response, 'Hi I should not be on this page!')
        self.assertEqual(no_response.status_code, 404)

    def test_seller_update_page_redirectos_for_anonymous_user(self):
        response = self.client.get(self.seller.get_update_url())
        no_response = self.client.get('/sellers/1234/update/')

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'sellers/seller_update_form.html')
        self.assertEqual(no_response.status_code, 404)

    def test_seller_update_resolve_sellerupdateview(self):
        view = resolve(self.seller.get_update_url())
        self.assertEqual(view.func.__name__, SellerUpdate.as_view().__name__)


class SellerDeleteTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.seller = SellerFactory(owner=self.user)

    def test_seller_delete_page_works_for_logged_in_user(self):
        self.client.force_login(self.user)
        response = self.client.get(self.seller.get_delete_url())
        no_response = self.client.get('/sellers/1234/delete/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sellers/seller_confirm_delete.html')
        self.assertContains(response, 'Delete')
        self.assertNotContains(response, 'Hi I should not be on this page!')
        self.assertEqual(no_response.status_code, 404)

    def test_seller_delete_with_valid_post_data_deletes_the_seller(self):
        self.assertEqual(Seller.objects.count(), 1)

        self.client.force_login(self.user)
        response = self.client.post(self.seller.get_delete_url())

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Seller.objects.count(), 0)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Seller was deleted successfully!")

    def test_seller_delete_for_non_existing_seller_routes_to_not_found(self):
        non_existing_seller_url = self.seller.get_delete_url()
        self.assertEqual(Seller.objects.count(), 1)

        Seller.objects.all().delete()

        self.client.login(self.user)
        response = self.client.get(non_existing_seller_url)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    def test_seller_delete_with_valid_post_for_non_existing_seller_routes_to_not_found(self):
        seller_url = self.seller.get_delete_url()
        Seller.objects.all().delete()

        self.assertEqual(Seller.objects.count(), 0)
        self.client.force_login(self.user)
        response = self.client.post(seller_url)

        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    def test_seller_delete_page_redirects_for_anonymous_user(self):
        response = self.client.get(self.seller.get_delete_url())
        no_response = self.client.get('/sellers/1234/delete/')

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'sellers/seller_confirm_delete.html')
        self.assertEqual(no_response.status_code, 404)

    def test_seller_delete_view_resolves_sellerdeleteview(self):
        view = resolve(self.seller.get_delete_url())
        self.assertEqual(view.func.__name__, SellerDelete.as_view().__name__)
