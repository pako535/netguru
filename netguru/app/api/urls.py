from django.conf.urls import url
from ..views import MovieListView

urlpatterns = [
    url(r'^movie/$', MovieListView.as_view(), name='movie_list')
]