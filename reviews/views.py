from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Movie, Review, Topic, MovieTopics
from .forms import ReviewForm

import datetime

# Create your views here.
def review_list(request):
	latest_review_list = Review.objects.order_by('-pub_date')[:9]
	context = {'latest_review_list':latest_review_list}
	return render(request, 'reviews/review_list.html', context)

def review_detail(request, review_id):
	review = get_object_or_404(Review, pk=review_id)
	return render(request, 'reviews/review_detail.html', {'review': review})

def movie_list(request):
	movie_list = Movie.objects.order_by('-date_released')
	context = {'movie_list': movie_list}
	return render(request, 'reviews/movie_list.html', context)

def topic_list(request):
	topic_list = Topic.objects.order_by('description')
	context = {'topic_list': topic_list}
	return render(request, 'reviews/topic_list.html', context)

def top10(request):
	movies = Movie.objects.all()
	ids = []
	ratings = []
	for x in movies:
		ids.append(x.movie_id)
		ratings.append(x.average_rating())
	z = zip(ids, ratings)
	z = sorted(z, key=lambda x: x[1])
	top10_list = []
	for x in z:
		top10_list.append(Movie.objects.get(movie_id=x[0]))
	context = {'movie_list': top10_list[:10]}
	return render(request, 'reviews/movie_list.html', context)


def movie_detail(request, movie_id):
	movie = get_object_or_404(Movie, pk=movie_id)
	form = ReviewForm()
	context = {
		'movie': movie,
		'movie_id': movie.movie_id,
		'name': movie.name,
		'trailer': movie.trailer_url,
		'poster': movie.poster_url,
		'date_released': movie.date_released,
		'topics': movie.topics,
		'form': form,
	}
	return render(request, 'reviews/movie_detail.html', context)

def topic_movie_list(request, topic_id):
	topic = get_object_or_404(Topic, pk=topic_id)
	movie_list = MovieTopics.objects.filter(topic=topic_id)
	movie_ids = []
	for x in movie_list:
		movie_ids.append(x.movie)
	context = {'movie_list': movie_ids}
	return render(request, 'reviews/movie_list.html', context)

@login_required
def add_review(request, movie_id):
	movie = get_object_or_404(Movie, pk=movie_id)
	form = ReviewForm(request.POST)
	if form.is_valid():
		rating = form.cleaned_data['rating']
		comment = form.cleaned_data['comment']
		user_name = request.user.username
		review = Review()
		review.movie = movie
		review.user_name = user_name
		review.rating = rating
		review.comment = comment
		review.pub_date = datetime.datetime.now()
		review.save()

		return HttpResponseRedirect(reverse('reviews:movie_detail', args=(movie_id,)))

	context = {
		'movie_id': movie.movie_id,
		'name': movie.name,
		'trailer': movie.trailer_url,
		'poster': movie.poster_url,
		'date_released': movie.date_released,
		'topics': movie.topics,
		'form': form,
	}
	return render(request, 'reviews/movie_detail.html', context)

def user_review_list(request, username=None):
	if not username:
		username = request.user.username
	latest_review_list = Review.objects.filter(user_name=username).order_by('-pub_date')
	context = {'latest_review_list': latest_review_list, 'username':username}
	return render(request, 'reviews/user_review_list.html', context)

def user_recommendation_list(request):
	return render(request, 'reviews/user_recommendation_list.html', {'username': request.user.username})