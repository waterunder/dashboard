from django.urls import path

from .views import DashboardPageView

urlpatterns = [
    path('', DashboardPageView.as_view(), name='dashboard'),
]
