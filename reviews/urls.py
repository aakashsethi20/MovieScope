from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.movie_list, name='movie_list'),
	url(r'^movie/(?P<movie_id>[0-9]+)/$', views.movie_detail, name='movie_detail'),
	url(r'^movie/(?P<movie_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
	url(r'^review/$', views.review_list, name='review_list'),
	url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
	url(r'^review/user/$', views.user_review_list, name='user_review_list'),
	url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
	url(r'^recommendation/$', views.user_recommendation_list, name='user_recommendation_list'),
	url(r'^topic/$', views.topic_list, name="topic_list"),
	url(r'^topic/(?P<topic_id>[0-9]+)/$', views.topic_movie_list, name='topic_movies'),
	url(r'^top10/$', views.top10, name='top10'),
	url(r'^actor/(?P<actor_id>[0-9]+)/$', views.actor_movie_list, name='actor_movie_list'),
	url(r'^director/(?P<director_id>[0-9]+)/$', views.director_movie_list, name='director_movie_list'),
]