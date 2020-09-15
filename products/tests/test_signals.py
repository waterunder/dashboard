from django.core.files.images import ImageFile
from django.test import TestCase

from products.factories import ProductFactory
from products.models import ProductImage
from sellers.factories import SellerFactory, UserFactory


class TestSignal(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.seller = SellerFactory(owner=self.user)
        self.product = ProductFactory(seller=self.seller)

    def test_thumbnails_are_generated_on_save(self):

        with open('products/fixtures/the-cathedral-the-bazaar.jpg', 'rb') as f:
            image = ProductImage(
                product=self.product,
                image=ImageFile(f, name='tctb.jpg'),
            )
            with self.assertLogs('products.signals', level='INFO') as cm:
                image.save()

        self.assertGreaterEqual(len(cm.output), 1)
        image.refresh_from_db()

        with open('products/fixtures/the-cathedral-the-bazaar.thumb.jpg', 'rb') as f:
            expected_content = f.read()
            assert image.thumbnail.read() == expected_content

        image.thumbnail.delete(save=False)
        image.image.delete(save=False)
