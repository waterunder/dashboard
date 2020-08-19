from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from products.models import Product, Review
from products.views import (
    ProductDelete,
    ProductDetailView,
    ProductListView,
    ProductUpdate,
    SearchResultsListView,
    SellerProductList,
)
from sellers.models import Seller


class ProductTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123',
        )
        self.seller = Seller.objects.create(
            name='Test-Company-LLC',
            description='Top worldwide experts in selling',
            email='testcompany@email.com',
            address1='Av de Mayo 855, portaldelsur, CABA',
            zip_code='1086',
            city='Buenos Aires',
            country='uk',
            owner=self.user,
        )
        self.product = Product.objects.create(
            title='Kepler155B',
            description='The first exoplanet found',
            price='250.00',
            seller=self.seller)

        self.review = Review.objects.create(
            product=self.product,
            review='highly recommended!',
            author=self.user,
        )

    def test_product_listing(self):
        self.assertEqual(f'{self.product.title}', 'Kepler155B')
        self.assertEqual(f'{self.product.description}', 'The first exoplanet found')
        self.assertEqual(f'{self.product.price}', '250.00')

    def test_product_list_view_redirects_for_anonymous_user(self):
        response = self.client.get(reverse('product_list'))
        no_response = self.client.get('/product/')

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'products/product_list.html')
        self.assertEqual(no_response.status_code, 404)

    def test_product_list_view_works_for_logged_in_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('product_list'))
        no_response = self.client.get('/product/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')
        self.assertContains(response, 'Products')
        self.assertNotContains(response, 'Hi I should not be on this page!')
        self.assertEqual(no_response.status_code, 404)

    def test_product_list_resolves_productlistview(self):
        view = resolve(reverse('product_list'))
        self.assertEqual(view.func.__name__, ProductListView.as_view().__name__)

    def test_product_detail_view_redirects_for_anonymous_user(self):
        response = self.client.get(self.product.get_absolute_url())
        no_response = self.client.get('/product/1234/')

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'products/product_detail.html')
        self.assertEqual(no_response.status_code, 404)

    def test_product_detail_view_works_for_logged_in_user(self):
        self.client.force_login(self.user)
        response = self.client.get(self.product.get_absolute_url())
        no_response = self.client.get('/products/1234/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Kepler')
        self.assertContains(response, 'highly recommended!')
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertEqual(no_response.status_code, 404)

    def test_product_detail_resolve_productdetailview(self):
        view = resolve(self.product.get_absolute_url())
        self.assertEqual(view.func.__name__, ProductDetailView.as_view().__name__)

    def test_seller_product_list_view_redirects_for_anonymous_user(self):
        response = self.client.get(reverse('seller_product_list', args=[str(self.seller.name)]))
        no_response = self.client.get('/product/dummy-seller/')

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'products/products_by_seller.html')
        self.assertEqual(no_response.status_code, 404)

    def test_seller_product_list_view_works_for_logged_in_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('seller_product_list', args=[str(self.seller.name)]))
        no_response = self.client.get('/products/dummy-seller/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.seller.name)
        self.assertNotContains(response, 'hi I should not be on this page!')
        self.assertTemplateUsed(response, 'products/products_by_seller.html')
        self.assertEqual(no_response.status_code, 404)

    def test_seller_product_list_resolves_sellerproductlistview(self):
        view = resolve(reverse('seller_product_list', args=[str(self.seller.name)]))
        self.assertEqual(view.func.__name__, SellerProductList.as_view().__name__)

    def test_product_update_page_works_for_logged_in_user(self):
        self.client.force_login(self.user)
        response = self.client.get(self.product.get_update_url())
        no_response = self.client.get('/products/1234/update/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_update_form.html')
        self.assertContains(response, 'Edit')
        self.assertNotContains(response, 'Hi I should not be on this page')
        self.assertEqual(no_response.status_code, 404)

    def test_product_update_page_redirects_for_anonymous_user(self):
        response = self.client.get(self.product.get_update_url())
        no_response = self.client.get('/products/1234/update/')

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'products/product_update_form.html')
        self.assertEqual(no_response.status_code, 404)

    def test_product_update_resolves_product_update_view(self):
        view = resolve(self.product.get_update_url())
        self.assertEqual(view.func.__name__, ProductUpdate.as_view().__name__)

    def test_product_delete_page_works_for_logged_in_user(self):
        self.client.force_login(self.user)
        response = self.client.get(self.product.get_delete_url())
        no_response = self.client.get('/products/1243/delete/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_confirm_delete.html')
        self.assertContains(response, 'delete')
        self.assertContains(response, 'Confirm')
        self.assertNotContains(response, 'Hi I should not be on this page!')
        self.assertEqual(no_response.status_code, 404)

    def test_product_delete_page_redirects_for_anonymous_user(self):
        response = self.client.get(self.product.get_delete_url())
        no_response = self.client.get('/products/1243/delete/')

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'products/product_confirm_delete.html')
        self.assertEqual(no_response.status_code, 404)

    def test_product_delete_resolves_product_delete_view(self):
        view = resolve(self.product.get_delete_url())
        self.assertEqual(view.func.__name__, ProductDelete.as_view().__name__)

    def test_search_results_page_works_for_logged_in_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('search_results'), {'q': 'count'})
        no_response = self.client.get('/search/', {'q': 'count'})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/search_results.html')
        self.assertContains(response, 'Search')
        self.assertNotContains(response, 'Hi I should not be on this page!')
        self.assertEqual(no_response.status_code, 404)

    def test_search_results_page_redirects_for_anonymous_user(self):
        response = self.client.get(reverse('search_results'), {'q': 'count'})
        no_response = self.client.get('/search/', {'q': 'count'})

        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'products/search_results.html')
        self.assertEqual(no_response.status_code, 404)

    def test_search_results_resolve_searchresultsview(self):
        view = resolve('/products/search/')
        self.assertEqual(view.func.__name__, SearchResultsListView.as_view().__name__)
