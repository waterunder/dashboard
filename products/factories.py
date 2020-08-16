import random

import factory

from products.models import Product
from sellers.models import Seller

sellers = Seller.objects.all()


class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    title = factory.Faker('word')
    description = factory.Faker('sentence')
    price = factory.Faker('random_int')
    active = factory.Faker('boolean')
    in_stock = factory.Faker('boolean')
    seller = random.choice(sellers)
