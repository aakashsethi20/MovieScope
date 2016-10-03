from __future__ import unicode_literals
from django.db import models
import numpy as np
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# Create your models here.
class Topic(models.Model):
	topic_id = models.AutoField(primary_key=True)
	description = models.CharField(max_length=20)
	#profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)

	class Meta:
		db_table = 'Topic'

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now())
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)

class Movie(models.Model):
	movie_id = models.AutoField(primary_key=True)
	name = models.CharField("Movie's name", max_length=70, unique=True)
	trailer_url = models.URLField("Movie's Trailer", default="")
	poster_url = models.URLField("Movie's Poster", default="")
	date_released = models.DateField("Movie's Release Date")
	topics = models.ManyToManyField(Topic, through='MovieTopics')
	#users = models.ManyToManyField('User', through='Watches')

	def average_rating(self):
		all_ratings = map(lambda x: x.rating, self.review_set.all())
		return np.mean(all_ratings)

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = "Movie"

class MovieTopics(models.Model):
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	language = models.CharField(max_length=50, default="English")
	SUBTITLES_CHOICES = (
		('Y', 'Yes'),
		('N', 'No'),
	)
	subtitles = models.CharField(max_length=1, choices=SUBTITLES_CHOICES, default='N')

	class Meta:
		db_table = "MovieTopics"
		unique_together = (("movie", "topic"),)


# class Watches(models.Model):
# 	#user = models.ForeignKey('User', on_delete=models.CASCADE)
# 	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
# 	date = models.DateField("Watched On")
# 	rating = models.IntegerField(validators=[MinValueValidator(0),
#                                        MaxValueValidator(5)], default=0)

# 	class Meta:
# 		db_table = "Watches"
# 		#unique_together = (("user", "movie"),)

class Actor(models.Model):
	actor_id = models.AutoField(primary_key=True)
	first_name = models.CharField("Actor's first name", max_length=50)
	last_name = models.CharField("Actor's last name", max_length=50)
	date_of_birth = models.DateField("Actor's DOB")
	movies = models.ManyToManyField(Movie, through='ActorPlays')
	
	class Meta:
		db_table = "Actor"

class Role(models.Model):
	role_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

	class Meta:
		db_table = "Role"

class ActorPlays(models.Model):
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

	class Meta:
		db_table = "ActorPlays"
		unique_together = (("movie", "actor"),)

class Director(models.Model):
	director_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	movies = models.ManyToManyField(Movie, through='Directs')

	class Meta:
		db_table = "Director"

class Directs(models.Model):
	director = models.ForeignKey(Director, on_delete=models.CASCADE)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

	class Meta:
		db_table = "Directs"
		unique_together = (("director", "movie"),)

class Studio(models.Model):
	studio_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	movies = models.ManyToManyField(Movie, through='Sponsors')

	class Meta:
		db_table = "Studio"

class Sponsors(models.Model):
	studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

	class Meta:
		db_table = "Sponsors"
		unique_together = (("studio", "movie"),)

class Cluster(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def get_members(self):
        return "\n".join([u.username for u in self.users.all()])