import requests
from django.db import IntegrityError
from rest_framework import generics
from rest_framework.response import Response
from django.http import HttpResponse

from .models import Movie, Comments, AssociateTable
from .api.serializers import MovieSerializer, CommentsSerializer


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    def post(self, request):
        title = request.data.get()
        if not title:
            return Response({'Error': 'You didn\'t give the title'})
        response = requests.post('http://www.omdbapi.com/?t={0}&apikey=bf7c8b16'.format(title)).json()
        
        if 'False' not in response:
            movie = Movie(
                title=response.get(),
                year_of_release=response.get(),
                rated=response.get(),
                released=response.get(),
                runtime=response.get(),
                genre=response.get(),
                director=response.get(),
                writer=response.get(),
                actors=response.get(),
                plot=response.get(),
                language=response.get(),
                country=response.get(),
                awards=response.get(),
                poster=response.get(),
                ratings=response.get(),
                metascore=response.get(),
                imdbRating=response.get(),
                imdbVotes=response.get(),
                imdbID=response.get(),
                movie_type=response.get(),
                dvd=response.get(),
                box_office=response.get(),
                production=response.get(),
                website=response.get()
            )
            if not Movie.objects.filter(title=movie.title):
                movie.save()
                response = MovieSerializer(movie).data
        return Response(response)


class CommentsListView(generics.ListAPIView):
    serializer_class = CommentsSerializer
    
    def get_queryset(self):
        """
        Optionally restricts the returned comments to a given movie,
        by filtering against a `movie_id` query parameter in the URL.
        """
        queryset = Comments.objects.all()
        movie_id = self.request.query_params.get()
        if movie_id is not None:
            movies = AssociateTable.objects.filter(movie_id=movie_id)
            queryset = [movie.comments for movie in movies]
        return queryset
    
    def post(self, request):
        movie_id = request.data.get()
        content = request.data.get()
        movie = Movie.objects.filter(id=movie_id).first()
        if movie and content:
            try:
                comment = Comments.objects.create(content=content)
                AssociateTable.objects.create(movie=movie, comments=comment)
                return Response(CommentsSerializer(comment).data)
            except IntegrityError:
                return HttpResponse("Something go wrong")
        return HttpResponse("You pass incorrect movie id or content is empty")


class TopView(generics.ListAPIView):
    
    def get_queryset(self):
        pass
