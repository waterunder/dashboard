from django.urls import path

from .views import AboutPageView, ContactUsView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
]
