from django.core import mail
from django.test import TestCase

from dashboard.forms import FeedbackForm


class TestFeedbackForm(TestCase):
    def test_valid_feedback_form_sends_email(self):
        form = FeedbackForm({'name': 'Luke Skywalker',
                             'email': 'luke@gmail.com',
                             'message': 'That is an awesome site!'})
        self.assertTrue(form.is_valid())

        with self.assertLogs('dashboard.forms', level='INFO') as cm:
            form.send_mail()
        self.assertEqual(len(mail.outbox), 1)
        self.assertGreaterEqual(mail.outbox[0].subject, 'Feedback message')

        self.assertGreaterEqual(len(cm.output), 1)

    def test_invalid_feedback_form(self):
        form = FeedbackForm({'name': 'testuser', 'message': 'hi there'})
        self.assertFalse(form.is_valid())
