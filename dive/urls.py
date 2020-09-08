from dive.views import DiveCreate, DiveDelete, DiveDetailView, DiveListView, DiveUpdate
from django.urls import path

urlpatterns = [
    path('', DiveListView.as_view(), name='dive_list'),
    path('<uuid:pk>/', DiveDetailView.as_view(), name='dive_detail'),
    path('create/', DiveCreate.as_view(), name='dive_create'),
    path('<uuid:pk>/update/', DiveUpdate.as_view(), name='dive_update'),
    path('<uuid:pk>/delete/', DiveDelete.as_view(), name='dive_delete'),
]
