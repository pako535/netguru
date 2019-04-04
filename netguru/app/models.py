from django.db import models


class Comments(models.Model):
    content = models.CharField(verbose_name='Content of comment', max_length=1000)


class Movie(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    year_of_release = models.CharField(verbose_name='Year', max_length=4)
    rated = models.CharField(verbose_name='Rated', max_length=10)
    released = models.CharField(verbose_name='Released', max_length=15)
    runtime = models.CharField(verbose_name='Runtime', max_length=15)
    genre = models.CharField(verbose_name='Genre', max_length=100)
    director = models.CharField(verbose_name='Director', max_length=50)
    writer = models.CharField(verbose_name='Writer', max_length=600)
    actors = models.CharField(verbose_name='Actros', max_length=100)
    plot = models.CharField(verbose_name='Plot', max_length=300)
    language = models.CharField(verbose_name='Language', max_length=50)
    country = models.CharField(verbose_name='Country', max_length=50)
    awards = models.CharField(verbose_name='Awards', max_length=200)
    poster = models.URLField(verbose_name='Poster')
    ratings = models.CharField(verbose_name='Ratings', max_length=300)
    metascore = models.CharField(verbose_name='Metascore', max_length=15)
    imdbRating = models.CharField(verbose_name='imdbRating', max_length=15)
    imdbVotes = models.CharField(verbose_name='imdbVotes', max_length=15)
    imdbID = models.CharField(verbose_name='imdbID', max_length=30)
    movie_type = models.CharField(verbose_name='Type', max_length=10)
    dvd = models.CharField(verbose_name='DVD', max_length=15)
    box_office = models.CharField(verbose_name='BoxOffice', max_length=15)
    production = models.CharField(verbose_name='Production', max_length=100)
    website = models.URLField(verbose_name="Website")
    rank = models.IntegerField(verbose_name="Rank", default=0)


class AssociateTable(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Movie")
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, verbose_name="Commnets")
