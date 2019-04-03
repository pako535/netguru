from rest_framework import serializers
from ..models import Comments, Movie, AssociateTable


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title')


class CommentsSerializer(serializers.ModelSerializer):
    movie_id = serializers.IntegerField(write_only=True, required=True)
    
    class Meta:
        model = Comments
        fields = ('id', 'content', 'movie_id')
