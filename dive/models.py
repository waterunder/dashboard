import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Dive(models.Model):
    NEGLIGIBLE = 0
    SMALL = 10
    MEDIUM = 20
    LARGE = 30

    WAVES = (
        (NEGLIGIBLE, "Negligible"),
        (SMALL, "Small"),
        (MEDIUM, "Medium"),
        (LARGE, "Large"),
    )

    CURRENT = (
        (NEGLIGIBLE, "Negligible"),
        (SMALL, "Light"),
        (MEDIUM, "Medium"),
        (LARGE, "Strong"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, blank=True)
    date = models.DateField()
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    visibility = models.PositiveIntegerField(default=20)
    bottom_time = models.PositiveIntegerField(default=30)
    avg_depth = models.PositiveIntegerField(default=10)
    max_depth = models.IntegerField(default=30)

    waves = models.IntegerField(choices=WAVES, default=SMALL)
    current = models.IntegerField(choices=CURRENT, default=SMALL)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('dive_detail', args=[str(self.id)])

    def get_update_url(self):
        return reverse('dive_update', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('dive_delete', args=[str(self.id)])
