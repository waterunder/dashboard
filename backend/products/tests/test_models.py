from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from products.factories import ProductFactory
from products.models import Product
from sellers.factories import SellerFactory, UserFactory


class ProductModelTests(TestCase):
    def setUp(self):
        self.superuser = get_user_model().objects.create_superuser(
            username='superuser',
            email='superuser@email.com',
            password='superpass123'
        )
        self.user_1 = UserFactory()
        self.user_2 = UserFactory()

        self.seller_1 = SellerFactory(owner=self.user_1)
        self.seller_2 = SellerFactory(owner=self.user_2)

        self.product_1 = ProductFactory(seller=self.seller_1)
        self.product_2 = ProductFactory(seller=self.seller_2)

    def test_product_model_listing(self):
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(self.product_1.seller, self.seller_1)
        self.assertEqual(self.product_2.seller, self.seller_2)

        self.assertEqual(self.product_1.seller.owner, self.user_1)
        self.assertEqual(self.product_2.seller.owner, self.user_2)

    def test_only_user_who_created_the_product_can_update_it(self):
        self.assertTrue(self.product_1.can_update(self.user_1))
        self.assertTrue(self.product_2.can_update(self.user_2))

        self.assertFalse(self.product_1.can_update(self.user_2))
        self.assertFalse(self.product_2.can_update(self.user_1))

    def test_only_user_who_created_the_product_can_delete_it(self):
        self.assertTrue(self.product_1.can_delete(self.user_1))
        self.assertTrue(self.product_2.can_delete(self.user_2))

        self.assertFalse(self.product_1.can_delete(self.user_2))
        self.assertFalse(self.product_2.can_delete(self.user_1))

    def test_superuser_can_update_any_product(self):
        self.assertTrue(self.product_1.can_update(self.superuser))
        self.assertTrue(self.product_2.can_update(self.superuser))

    def test_superuser_can_delete_any_product(self):
        self.assertTrue(self.product_1.can_delete(self.superuser))
        self.assertTrue(self.product_2.can_delete(self.superuser))

    def test_most_recent_products_are_listed_first(self):
        yesterday = timezone.now() + timezone.timedelta(days=-1)
        last_week = timezone.now() + timezone.timedelta(days=-7)

        self.product_1.date_updated = last_week
        self.product_2.date_updated = yesterday

        self.product_1.save()
        self.product_2.save()

        latest_product = Product.objects.all()[0]
        self.assertEqual(latest_product, self.product_2)
