from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from dashboard.forms import FeedbackForm


class DashboardPageView(TemplateView):
    template_name = 'dashboard/index.html'


class IconsPageView(TemplateView):
    template_name = 'dashboard/icons.html'


class FormsPageView(TemplateView):
    template_name = 'dashboard/forms.html'


class TablesPageView(TemplateView):
    template_name = 'dashboard/tables.html'


class CalendarPageView(TemplateView):
    template_name = 'dashboard/calendar.html'


class ProfilePageView(TemplateView):
    template_name = 'dashboard/profile.html'


class FeedbackFormView(SuccessMessageMixin, FormView):
    template_name = 'dashboard/feedback.html'
    form_class = FeedbackForm
    success_message = 'Feedback sent successfully!'
    success_url = '/'

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)
