from django.views.generic import TemplateView


class Logbook(TemplateView):
    template_name = 'dive/logbook.html'
