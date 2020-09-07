from random import choice

import factory
from django.contrib.auth import get_user_model

from sellers.models import Seller


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    username = factory.Faker('user_name')


class SellerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Seller

    name = factory.Faker('company')
    description = factory.Faker('sentence')
    email = factory.Faker('email')
    address1 = factory.Faker('address')
    address2 = factory.Faker('address')
    zip_code = factory.Faker('zipcode')
    city = factory.Faker('city')
    country = choice(['ar', 'uk', 'us'])
    is_mock = factory.Faker('boolean')
    is_active = factory.Faker('boolean')
    logo = factory.Faker('image_url')
    header_image = factory.Faker('image_url')
    owner = factory.SubFactory(UserFactory)
