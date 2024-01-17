from django.urls import path
from .views import SalleListView

urlpatterns=[
    path('',SalleListView.as_view(),name="Administrator")
]
