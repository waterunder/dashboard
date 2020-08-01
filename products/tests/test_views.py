from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from products.models import Product, Review
from sellers.models import Seller


class ProductTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com',
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

    def test_product_list_view(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Kepler')
        self.assertTemplateUsed(response, 'dashboard/product_list.html')

    def test_product_detail_view(self):
        response = self.client.get(self.product.get_absolute_url())
        no_response = self.client.get('/products/1234/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Kepler')
        self.assertContains(response, 'highly recommended!')
        self.assertTemplateUsed(response, 'products/product_detail.html')

        self.assertEqual(no_response.status_code, 404)
