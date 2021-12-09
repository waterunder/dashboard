import factory

from products.models import Product
from sellers.factories import SellerFactory


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Faker('word')
    description = factory.Faker('sentence')
    price = factory.Faker('random_int')
    active = factory.Faker('boolean')
    in_stock = factory.Faker('boolean')
    seller = factory.SubFactory(SellerFactory)
