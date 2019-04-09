from django.shortcuts import render
from rest_framework import generics
from .models import Make
from .serializers import MakeSerializer


class ListMakeView(generics.ListAPIView):
    """
    Provides a get method handler.
    """

    queryset = Make.objects.all()
    serializer_class = MakeSerializer