from django.test import TestCase
from django.urls import reverse

from .models import Product


class ProductTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            title='Kepler155B', description='The first exoplanet found', price='250.00',)

    def test_book_listing(self):
        self.assertEqual(f'{self.product.title}', 'Kepler155B')
        self.assertEqual(f'{self.product.description}', 'The first exoplanet found')
        self.assertEqual(f'{self.product.price}', '250.00')

    def test_book_list_view(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Kepler')
        self.assertTemplateUsed(response, 'products/product_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.product.get_absolute_url())
        no_response = self.client.get('/products/1234/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Kepler')
        self.assertTemplateUsed(response, 'products/product_detail.html')

        self.assertEqual(no_response.status_code, 404)
