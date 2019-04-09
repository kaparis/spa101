from django.urls import path
from .views import ListMakeView


urlpatterns = [
    path('makes/', ListMakeView.as_view(), name="make-all")
]