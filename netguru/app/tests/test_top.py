from app.models import Movie, Comments, CommentsForMovie
from app.api.serializers import CommentsSerializer
from .base import BaseTest


class TopTest(BaseTest):
    
    @classmethod
    def setUpClass(cls):
        super(TopTest, cls).setUpClass()
        cls.TOP_URL = '/top/'
    
    def setUp(self):
        movies_url = '/movies/'
        comments_url = '/comments/'
        self.client.post(movies_url, data={'title': "Guardians of the Galaxy Vol. 2"})
        self.client.post(movies_url, data={'title': "Blade"})
        self.client.post(movies_url, data={'title': "Czterej"})
        self.client.post(comments_url, {'movie_id': 1, 'content': "Comment #1"})
        self.client.post(comments_url, {'movie_id': 1, 'content': "Comment #2"})
        self.client.post(comments_url, {'movie_id': 2, 'content': "Comment #3"})
        self.client.post(comments_url, {'movie_id': 2, 'content': "Comment #4"})
        self.client.post(comments_url, {'movie_id': 3, 'content': "Comment #5"})
    
    def assertResponseMovieIdWithDB(self, response, movies):
        for resp, movie in zip(response.data, movies):
            self.assertEqual(resp.get('movie_id'), movie.id)
    
    def test_get_top_without_range(self):
        response = self.client.get(self.TOP_URL)
        self.assertContains(response, 'You must enter the beginning and end of the data range')
    
    def test_get_large_range(self):
        response = self.client.get(self.TOP_URL + '?start_date=0&end_date=2030')
        movies = Movie.objects.all()
        self.assertResponseMovieIdWithDB(response, movies)
    
    def test_get_filter_one_movie_by_range(self):
        movie = Movie.objects.all().first()
        response = self.client.get(self.TOP_URL + '?start_date={0}&end_date={1}'.format(movie.year_of_release,
                                                                                        movie.year_of_release))
        self.assertEqual(response.data[0].get('movie_id'), movie.id)
