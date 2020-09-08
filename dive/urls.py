from dive.views import DiveDetailView, DiveListView
from django.urls import path

urlpatterns = [
    path('', DiveListView.as_view(), name='dive_list'),
    path('<uuid:pk>/', DiveDetailView.as_view(), name='dive_detail'),
]
