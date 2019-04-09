from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='make_index'),
    path('view', views.read, name='make_view'),
   
]