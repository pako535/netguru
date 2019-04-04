from django.conf.urls import url
from ..views import MovieListView, CommentsListView, TopListView

urlpatterns = [
    url(r'^movies/$', MovieListView.as_view(), name='movie_list'),
    url(r'^comments/$', CommentsListView.as_view(), name='comment_list'),
    url(r'^top/$', TopListView.as_view(), name='top'),
]
