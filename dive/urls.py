from dive.views import Logbook
from django.urls import path

urlpatterns = [
    path('logbook/', Logbook.as_view(), name='logbook'),
]
