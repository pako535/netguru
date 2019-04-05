import requests
from rest_framework import filters
from django.db import IntegrityError
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Movie, Comments, CommentsForMovie
from .api.serializers import MovieSerializer, CommentsSerializer


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'
    
    def post(self, request):
        title = request.data.get('title', 'None')
        if not title or title == 'None':
            return Response({'Error': 'You didn\'t give the title'})
        response = requests.post('http://www.omdbapi.com/?t={0}&apikey=bf7c8b16'.format(title)).json()
        
        if 'False' not in response and not Movie.objects.filter(title=response.get('Title', 'None')):
            movie = Movie(
                title=response.get('Title', 'None'),
                year_of_release=response.get('Year', 'None'),
                rated=response.get('Rated', 'None'),
                released=response.get('Released', 'None'),
                runtime=response.get('Runtime', 'None'),
                genre=response.get('Genre', 'None'),
                director=response.get('Director', 'None'),
                writer=response.get('Writer', 'None'),
                actors=response.get('Actors', 'None'),
                plot=response.get('Plot', 'None'),
                language=response.get('Language', 'None'),
                country=response.get('Country', 'None'),
                awards=response.get('Awards', 'None'),
                poster=response.get('Poster', 'None'),
                ratings=response.get('Ratings', 'None'),
                metascore=response.get('Metascore', 'None'),
                imdbRating=response.get('imdbRating', 'None'),
                imdbVotes=response.get('imdbVotes', 'None'),
                imdbID=response.get('imdbID', 'None'),
                movie_type=response.get('Type', 'None'),
                dvd=response.get('DVD', 'None'),
                box_office=response.get('BoxOffice', 'None'),
                production=response.get('Production', 'None'),
                website=response.get('Website', 'None')
            )
            movie.save()
            response = [MovieSerializer(movie).data]
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
            movies = CommentsForMovie.objects.filter(movie_id=movie_id)
            queryset = [movie.comments for movie in movies]
        return queryset
    
    def post(self, request):
        movie_id = request.data.get('movie_id')
        if not movie_id:
            return Response({'Error': 'You pass incorrect movie id'})
        content = request.data.get('content', "DUPA")
        movie = Movie.objects.filter(id=movie_id).first()
        if movie and content:
            try:
                comment = Comments.objects.create(content=content)
                CommentsForMovie.objects.create(movie=movie, comments=comment)
                return Response([CommentsSerializer(comment).data])
            except IntegrityError:
                return Response({'Error': 'Something go wrong'})
        return Response({'Error': 'You pass incorrect movie id or content is empty'})


class TopListView(APIView):
    
    def get(self, request):
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if not self._check_if_start_and_end_date_exist(start_date, end_date):
            return Response(
                dict(
                    message='You must enter the beginning and end of the data range '
                            'for eg. \'/top/?start_date=0&end_date=1\'',
                    start_date=start_date,
                    end_date=end_date
                )
            )
        
        response = self._prepare_response(start_date, end_date)
        return Response(response)
    
    @staticmethod
    def _prepare_response(start_date, end_date):
        movies = Movie.objects. \
            extra({'year_of_release_uint': 'CAST(year_of_release as UNSIGNED)'}). \
            filter(year_of_release__gte=start_date). \
            filter(year_of_release__lte=end_date). \
            order_by('-total_comments')
        response = []
        rank_counter = 0
        prev_total_comments = -1
        for movie in movies:
            if movie.total_comments != prev_total_comments:
                rank_counter += 1
                prev_total_comments = movie.total_comments
            response.append(dict(
                movie_id=movie.id,
                total_comments=movie.total_comments,
                rank=rank_counter))
        
        return response
    
    @staticmethod
    def _check_if_start_and_end_date_exist(start_date, end_date):
        if start_date is None and end_date is None:
            return False
        return True
