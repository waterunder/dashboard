
import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Seller(models.Model):
    SUPPORTED_COUNTRIES = (
        ("uk", "United Kingdom"),
        ("us", "United States of America"),
        ("ar", "Argentina"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    email = models.EmailField()
    address1 = models.CharField("Address line 1", max_length=60)
    address2 = models.CharField("Address line 2", max_length=60, blank=True)
    zip_code = models.CharField("ZIP / Postal code", max_length=12)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=3, choices=SUPPORTED_COUNTRIES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_mock = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    logo = models.ImageField(upload_to='sellers/logo/', blank=True, null=True)
    header_image = models.ImageField(upload_to='sellers/headerImage', blank=True, null=True)

    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='seller')

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return ", ".join(
            [
                self.name,
                self.address1,
                self.address2,
                self.zip_code,
                self.city,
                self.country,
            ]
        )

    def get_absolute_url(self):
        return reverse('seller_detail', args=[str(self.id)])

    def get_update_url(self):
        return reverse('seller_update', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('seller_delete', args=[str(self.id)])

    def can_delete(self, user):
        return user.is_superuser or self.owner == user

    def can_update(self, user):
        return user.is_superuser or self.owner == user
