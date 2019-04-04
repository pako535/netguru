from rest_framework import serializers
from ..models import Comments, Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MovieSerializer, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'title':
                self.fields[field].read_only = True


class CommentsSerializer(serializers.ModelSerializer):
    movie_id = serializers.IntegerField(write_only=True, required=True)
    
    class Meta:
        model = Comments
        fields = ('id', 'content', 'movie_id')
