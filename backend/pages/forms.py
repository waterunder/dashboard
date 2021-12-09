import logging

from django import forms
from django.conf import settings
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', max_length=600, widget=forms.Textarea)

    def send_mail(self):
        logger.info('Sending email...')
        message = 'From: {0}\n{1}\n{2}'.format(
            self.cleaned_data['name'],
            self.cleaned_data['email'],
            self.cleaned_data['message']
        )
        logger.info('message: %s', message)
        send_mail(subject='Site message',
                  message=message,
                  from_email='site@website.domain',
                  recipient_list=settings.RECIPIENT_LIST,
                  fail_silently=False)
