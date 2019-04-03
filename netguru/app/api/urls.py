from django.conf.urls import url
from ..views import MovieListView, CommentsListView

urlpatterns = [
    url(r'^movies/$', MovieListView.as_view(), name='movie_list'),
    url(r'^comments/$', CommentsListView.as_view(), name='comment_list'),
]
