from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.files.images import ImageFile
from django.test import TestCase

from products import models
from sellers.models import Seller


class TestSignal(TestCase):
    def test_thumbnails_are_generated_on_save(self):
        user = get_user_model().objects.all()[0]
        seller = Seller(name='The Royal Co.',
                        email='theroyal@email.com',
                        address1='155, BakerStreet, London',
                        zip_code='1001',
                        city='London',
                        country='uk',
                        owner=user)

        product = models.Product(
            title='The cathedral and the bazaar',
            description='A nice book',
            price=Decimal('10.00'),
            seller=seller,
        )
        product.save()

        with open('products/fixtures/the-cathedral-the-bazaar.jpg', 'rb') as f:
            image = models.ProductImage(
                product=product,
                image=ImageFile(f, name='tctb.jpg'),
            )
            with self.assertLogs('main', level='INFO') as cm:
                image.save()

        self.assertGreaterEqual(len(cm.output), 1)
        image.refresh_from_db()

        with open('products/fixtures/the-cathedral-the-bazaar.thumb.jpg', 'rb') as f:
            expected_content = f.read()
            assert image.thumbnail.read() == expected_content

        image.thumbnail.delete(save=False)
        image.image.delete(save=False)
