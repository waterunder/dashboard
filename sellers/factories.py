import random

import factory
from django.contrib.auth import get_user_model

from sellers.models import Seller

users = get_user_model().objects.all()


class SellerFactory(factory.Factory):
    class Meta:
        model = Seller

    name = factory.Faker('company')
    description = factory.Faker('sentence')
    email = factory.Faker('email')
    address1 = factory.Faker('address')
    address2 = factory.Faker('address')
    zip_code = factory.Faker('zipcode')
    city = factory.Faker('city')
    country = random.choice(['ar', 'uk', 'us'])
    is_mock = factory.Faker('boolean')
    is_active = factory.Faker('boolean')
    logo = factory.Faker('image_url')
    header_image = factory.Faker('image_url')
    owner = random.choice(users)
