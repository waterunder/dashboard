from django.views.generic import TemplateView


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


class LoginPageView(TemplateView):
    template_name = 'dashboard/login.html'


class RegisterPageView(TemplateView):
    template_name = 'dashboard/register.html'
