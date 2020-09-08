import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Dive(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    visibility = models.IntegerField()
    bottom_time = models.IntegerField()
    description = models.CharField(max_length=200, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)

    def get_absolute_url(self):
        return reverse('dive_detail', args=[str(self.id)])

    def get_update_url(self):
        return reverse('dive_update', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('dive_delete', args=[str(self.id)])
