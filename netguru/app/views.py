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
        title = request.data.get('title', None)
        response = requests.post('http://www.omdbapi.com/?t={0}&apikey=bf7c8b16'.format(title)).json()
        
        # Nie dublowanie sie filmow, validacja title, sprawdzic czy zwracam obiekt
        
        if 'False' in response and title:
            response = Movie.objects.create(
                title=response.get('Title'),
                year_of_release=response.get('Year'),
                rated=response.get('Rated'),
                released=response.get('Released'),
                runtime=response.get('Runtime'),
                genre=response.get('Genre'),
                director=response.get('Director'),
                writer=response.get('Writer'),
                actors=response.get('Actors'),
                plot=response.get('Plot'),
                language=response.get('Language'),
                country=response.get('Country'),
                awards=response.get('Awards'),
                poster=response.get('Poster'),
                ratings=response.get('Ratings'),
                metascore=response.get('Metascore'),
                imdbRating=response.get('imdbRating'),
                imdbVotes=response.get('imdbVotes'),
                imdbID=response.get('imdbID'),
                movie_type=response.get('Type'),
                dvd=response.get('DVD'),
                box_office=response.get('BoxOffice'),
                production=response.get('Production'),
                website=response.get('Website')
            )
        return Response(response)


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
    
    def post(self, request):
        movie_id = request.data.get('movie_id', None)
        content = request.data.get('content')
        movie = Movie.objects.filter(id=movie_id).first()
        if movie and content:
            try:
                comment = Comments.objects.create(content=content)
                AssociateTable.objects.create(movie=movie, comments=comment)
                return Response(CommentsSerializer(comment).data)
            except IntegrityError:
                return HttpResponse("Something go wrong")
        return HttpResponse("You pass incorrect movie id or content is empty")
