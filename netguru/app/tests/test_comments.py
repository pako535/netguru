from app.models import Movie, Comments, CommentsForMovie
from app.api.serializers import CommentsSerializer
from .base import BaseTest


class CommentsTest(BaseTest):
    
    @classmethod
    def setUpClass(cls):
        super(CommentsTest, cls).setUpClass()
        cls.COMMENTS_URL = '/comments/'
        movie = Movie.objects.create(
            title="Czterej Pancerni i pies",
            year_of_release="1966–",
            rated="N/A",
            released="N/A",
            runtime="55 min",
            genre="War, Adventure",
            director="N/A",
            writer="N/A",
            actors="Janusz Gajos, Franciszek Pieczka, Wlodzimierz Press, Malgorzata Niemirska",
            plot="Story follows the adventures of a tank crew and their T-34 tank in the "
                 "1st Polish Army during World War II.",
            language="Russian, Polish",
            country="Poland",
            awards="N/A",
            poster="https://images-na.ssl-images-amazon.com/images/M/MV5BODNmNzcwYWU"
                   "tMDMyZS00NTY5LTlmNDEtZTk3NmMzNjQzYjZhXkEyXkFqcGdeQXVyMTc4MzI2NQ@@._V1_SX300.jpg",
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
        comment = Comments.objects.create(content="Comment #1")
        CommentsForMovie.objects.create(movie=movie, comments=comment)
        Comments.objects.create(content="Comment #2")
    
    def test_get_comments(self):
        response = self.client.get(self.COMMENTS_URL)
        comments = Comments.objects.all()
        self.assertReponseWithModelInDB(response, comments, CommentsSerializer)
    
    def test_get_comments_with_set_movie_id(self):
        url = self.COMMENTS_URL + '?movie_id=1'
        response = self.client.get(url)
        comments = Comments.objects.filter(id=1)
        self.assertReponseWithModelInDB(response, comments, CommentsSerializer)
    
    def test_post_comment(self):
        content = "Comment #3"
        response = self.client.post(self.COMMENTS_URL, {'movie_id': 1,
                                                        'content': content})
        comment = Comments.objects.filter(content=content)
        self.assertIfObjectExist(comment)
        self.assertReponseWithModelInDB(response, comment, CommentsSerializer)
    
    def test_post_comment_without_movie_id(self):
        content = "Comment #3"
        response = self.client.post(self.COMMENTS_URL, {'content': content})
        comment = Comments.objects.filter(content=content)
        self.assertIfObjectNotExist(comment)
        self.assertContains(response, 'You pass incorrect movie id or content is empty')
