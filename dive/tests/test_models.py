from dive.factories import DiveFactory, UserFactory
from dive.models import Dive
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone


class DiveModelTests(TestCase):
    def setUp(self):
        self.superuser = get_user_model().objects.create_superuser(
            username='superuser',
            email='superuser@email.com',
            password='superpass123'
        )
        self.user_1 = UserFactory()
        self.user_2 = UserFactory()

        self.dive_1 = DiveFactory(created_by=self.user_1)

        self.dive_2 = DiveFactory(created_by=self.user_2)
        self.dive_3 = DiveFactory(created_by=self.user_2)

    def test_dive_model_creation(self):
        self.assertEqual(Dive.objects.count(), 3)
        self.assertEqual(self.dive_1.created_by, self.user_1)
        self.assertEqual(self.dive_2.created_by, self.user_2)
        self.assertEqual(self.dive_3.created_by, self.user_2)

    def test_most_recent_dives_are_listed_first(self):
        yesterday = timezone.now() + timezone.timedelta(days=-1)
        last_week = timezone.now() + timezone.timedelta(days=-7)
        today = timezone.now()

        self.dive_1.date = last_week
        self.dive_2.date = yesterday
        self.dive_3.date = today

        self.dive_1.save()
        self.dive_2.save()
        self.dive_3.save()

        latest_dive = Dive.objects.all()[0]
        self.assertEqual(latest_dive, self.dive_3)

    def test_only_user_who_created_a_dive_can_update_it(self):
        self.assertTrue(self.dive_1.can_update(self.user_1))
        self.assertTrue(self.dive_2.can_update(self.user_2))
        self.assertTrue(self.dive_3.can_update(self.user_2))

        self.assertFalse(self.dive_1.can_update(self.user_2))
        self.assertFalse(self.dive_2.can_update(self.user_1))
        self.assertFalse(self.dive_3.can_update(self.user_1))

    def test_only_user_who_created_a_dive_can_delete_it(self):
        self.assertTrue(self.dive_1.can_delete(self.user_1))
        self.assertTrue(self.dive_2.can_delete(self.user_2))
        self.assertTrue(self.dive_3.can_delete(self.user_2))

        self.assertFalse(self.dive_1.can_delete(self.user_2))
        self.assertFalse(self.dive_2.can_delete(self.user_1))
        self.assertFalse(self.dive_3.can_delete(self.user_1))

    def test_superuser_can_update_any_dive(self):
        self.assertTrue(self.dive_1.can_update(self.superuser))
        self.assertTrue(self.dive_2.can_update(self.superuser))
        self.assertTrue(self.dive_3.can_update(self.superuser))

    def test_superuser_can_delete_any_dive(self):
        self.assertTrue(self.dive_1.can_delete(self.superuser))
        self.assertTrue(self.dive_2.can_delete(self.superuser))
        self.assertTrue(self.dive_3.can_delete(self.superuser))
