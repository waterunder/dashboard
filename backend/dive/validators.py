from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_past_date(date):
    if date > timezone.now().date():
        raise ValidationError('Date cannot be in the future!')
