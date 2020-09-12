import uuid

from dive.validators import validate_past_date
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
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
    date = models.DateField(validators=[validate_past_date])
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    visibility = models.PositiveIntegerField(default=20, validators=[MaxValueValidator(1000)],
                                             help_text='Visibility in metres.')
    bottom_time = models.PositiveIntegerField(default=30, validators=[MaxValueValidator(3600)],
                                              help_text='Bottom time in minutes.')
    avg_depth = models.PositiveIntegerField(default=10, validators=[MaxValueValidator(5000)],
                                            help_text='Average dive depth in metres.')
    max_depth = models.PositiveIntegerField(default=30, validators=[MaxValueValidator(5000)])
    surface_temperature = models.PositiveIntegerField(default=30, validators=[MaxValueValidator(60)],
                                                      help_text='Surface temperature in degree celsius.')
    bottom_temperature = models.PositiveIntegerField(default=15, validators=[MaxValueValidator(60)],
                                                     help_text='Bottom temperature in degree celsius.')
    waves = models.IntegerField(choices=WAVES, default=SMALL)
    current = models.IntegerField(choices=CURRENT, default=SMALL)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='dives')

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

    def can_delete(self, user):
        return user.is_superuser or self.created_by == user

    def can_update(self, user):
        return user.is_superuser or self.created_by == user
