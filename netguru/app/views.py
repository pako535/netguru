from django.db import IntegrityError
from rest_framework import generics
from django.http import HttpResponse
from .models import Movie, Comments, AssociateTable
from .api.serializers import MovieSerializer, CommentsSerializer


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CommentsListView(generics.ListAPIView):
    serializer_class = CommentsSerializer
    
    def get_queryset(self):
        """
        Optionally restricts the returned comments to a given movie,
        by filtering against a `movie_id` query parameter in the URL.
        """
        queryset = Comments.objects.all()
        movie_id = self.request.query_params.get('movie_id', None)
        if movie_id is not None:
            movies = AssociateTable.objects.filter(movie_id=movie_id)
            queryset = [movie.comments for movie in movies]
        return queryset
    
    def post(self):
        movie_id = self.request.data.get('movie_id', None)
        content = self.request.data.get('content')
        movie = Movie.objects.filter(id=movie_id).first()
        if movie and content:
            try:
                comment = Comments.objects.create(content=content)
                AssociateTable.objects.create(movie=movie, comments=comment)
                return HttpResponse("Succes")
            except IntegrityError:
                return HttpResponse("Something go wrong")
        return HttpResponse("You pass incorrect movie id or content is empty")
