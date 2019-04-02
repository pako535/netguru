from django.shortcuts import render
from rest_framework import generics
from .models import Movie, Comments
from .api.serializers import MovieSerializer


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
