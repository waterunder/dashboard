from django.contrib.auth import get_user_model
from django.test import TestCase

from sellers.models import Seller


class SellerModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="testpass123",
        )
        self.seller = Seller.objects.create(
            name="Test Company LLC",
            description="The best company worldwide",
            email="testcompany@email.com",
            address1="baker street 555, London, UK",
            zip_code="1086",
            city="London",
            country="uk",
            owner=self.user
        )

    def test_seller_listing(self):
        self.assertEqual(f'{self.seller.name}', 'Test Company LLC')
        self.assertEqual(f'{self.seller.description}', 'The best company worldwide')
        self.assertEqual(f'{self.seller.email}', 'testcompany@email.com')
        self.assertEqual(f'{self.seller.address1}', 'baker street 555, London, UK')
        self.assertEqual(f'{self.seller.zip_code}', '1086')
        self.assertEqual(f'{self.seller.city}', 'London')
        self.assertEqual(self.seller.owner, self.user)
