from django.urls import path

from . import views

urlpatterns = [
    path('', views.DashboardPageView.as_view(), name='dashboard'),
    path('icons/', views.IconsPageView.as_view(), name='icons'),
    path('forms/', views.FormsPageView.as_view(), name='forms'),
    path('tables/', views.TablesPageView.as_view(), name='tables'),
    path('calendar/', views.CalendarPageView.as_view(), name='calendar'),
    path('profile/', views.ProfilePageView.as_view(), name='profile'),
    path('feedback/', views.FeedbackFormView.as_view(), name='feedback'),
]
