import logging

from django import forms
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


class ProductShareForm(forms.Form):
    to = forms.CharField(max_length=25)
    email = forms.EmailField()
    comments = forms.CharField(widget=forms.Textarea)

    def send_mail(self):
        logger.info('sending product share email...')
        subject = 'Hey...'
        message = 'Checkout this product'
        from_email = 'veerplaying@gmail.com',
        to_email = 'gurupratap.matharu@gmail.com'
        send_mail(subject=subject, message=message,
                  from_email=from_email,
                  recipient_list=[to_email, ],
                  fail_silently=False)
