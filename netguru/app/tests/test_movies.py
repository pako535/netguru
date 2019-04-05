from app.models import Movie
from app.api.serializers import MovieSerializer
from .base import BaseTest


class MoviesTest(BaseTest):
    
    @classmethod
    def setUpClass(cls):
        super(MoviesTest, cls).setUpClass()
        cls.MOVIES_URL = '/movies/'
        Movie.objects.create(
            title="Czterej Pancerni i pies",
            year_of_release="1966–",
            rated="N/A",
            released="N/A",
            runtime="55 min",
            genre="War, Adventure",
            director="N/A",
            writer="N/A",
            actors="Janusz Gajos, Franciszek Pieczka, Wlodzimierz Press, Malgorzata Niemirska",
            plot="Story follows the adventures of a tank crew and their T-34 tank in the"
                 " 1st Polish Army during World War II.",
            language="Russian, Polish",
            country="Poland",
            awards="N/A",
            poster="https://images-na.ssl-images-amazon.com/images/M/MV5BODNmNzcwYWUtMDM"
                   "yZS00NTY5LTlmNDEtZTk3NmMzNjQzYjZhXkEyXkFqcGdeQXVyMTc4MzI2NQ@@._V1_SX300.jpg",
            ratings="[{'Source': 'Internet Movie Database', 'Value': '8.0/10'}]",
            metascore="N/A",
            imdbRating="8.0",
            imdbVotes="871",
            imdbID="tt0120948",
            movie_type="series",
            dvd="None",
            box_office="None",
            production="None",
            website="None",
            total_comments=1
        )
        
    def test_get_movies(self):
        response = self.client.get(self.MOVIES_URL)
        movies = Movie.objects.all()
        self.assertReponseWithModelInDB(response, movies, MovieSerializer)
    
    def test_post_movies(self):
        title = "Guardians of the Galaxy Vol. 2"
        response = self.client.post(self.MOVIES_URL, data={'title': title})
        movie = Movie.objects.filter(title=title)
        self.assertIfObjectExist(movie)
        self.assertReponseWithModelInDB(response, movie, MovieSerializer)
    
    def test_post_without_title(self):
        response = self.client.post(self.MOVIES_URL)
        self.assertContains(response, 'You didn\'t give the title')
