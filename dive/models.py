import uuid

from django.db import models


class Dive(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dive_date = models.DateField()
