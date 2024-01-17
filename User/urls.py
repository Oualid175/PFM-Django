from django.urls import path
from .views import reserver,reservationsListView

urlpatterns = [
    path('reserver/', reserver, name='reserver'),
    path('ListesReservations/',reservationsListView.as_view(),name="User"),
]
