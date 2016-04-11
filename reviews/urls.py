from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.movie_list, name='movie_list'),
	url(r'^movie/(?P<movie_id>[0-9]+)/$', views.movie_detail, name='movie_detail'),
	url(r'^movie/(?P<movie_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
	url(r'^review$', views.review_list, name='review_list'),
	url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
	url(r'^review/user/$', views.user_review_list, name='user_review_list'),
	url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
	url(r'^recommendation/$', views.user_recommendation_list, name='user_recommendation_list'),
]