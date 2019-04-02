from django.db import models


class Comments(models.Model):
    content = models.CharField(verbose_name='Content of comment', max_length=1000)


class Movie(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    movie_type = models.CharField(verbose_name='Type', max_length=10)
    year_of_release = models.IntegerField(verbose_name='Year')
    data_type = models.CharField(verbose_name='Data type', max_length=4)
    page = models.IntegerField(verbose_name="Page")
    callback = models.CharField(verbose_name="JSONP callback name", max_length=100)
    version = models.CharField(verbose_name="API version", max_length=10)
    rank = models.IntegerField(verbose_name="Rank")
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, verbose_name="Commnets")




