from django.views.generic import DetailView, TemplateView

from users.models import Profile


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


class FeedbackPageView(TemplateView):
    template_name = 'dashboard/feedback.html'
