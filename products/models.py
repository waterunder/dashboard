import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from sellers.models import Seller


class ProductTagManager(models.Manager):
    def get_by_natural_key(self, slug):
        return self.get(slug=slug)


class ProductTag(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=48)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    objects = ProductTagManager()

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.slug,)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    active = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    date_updated = models.DateTimeField(auto_now=True)

    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='products')
    tags = models.ManyToManyField(ProductTag, blank=True, related_name='products')

    class Meta:
        permissions = [
            ('special_status', 'Can see all products'),
        ]
        ordering = ['-date_updated']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('product_delete', args=[str(self.id)])

    def get_update_url(self):
        return reverse('product_update', args=[str(self.id)])

    def can_update(self, user):
        return user.is_superuser or self.seller.owner == user

    def can_delete(self, user):
        return user.is_superuser or self.seller.owner == user


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product-images')
    thumbnail = models.ImageField(upload_to='product-thumbnails', null=True)

    def __str__(self):
        return self.image.url


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews',)
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.review
