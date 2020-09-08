import factory
from dive.models import Dive
from django.contrib.auth import get_user_model


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    username = factory.Faker('user_name')


class DiveFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Dive
    date = factory.Faker('date_this_year')
    lat = factory.Faker('latitude')
    lon = factory.Faker('longitude')
    visibility = factory.Faker('random_int')
    bottom_time = factory.Faker('random_int')
    description = factory.Faker('sentence')

    created_by = factory.SubFactory(UserFactory)
