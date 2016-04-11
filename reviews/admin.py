from django.contrib import admin
from .models import Movie, Review

class ReviewAdmin(admin.ModelAdmin):
	model = Review
	list_display = ('movie', 'rating', 'user_name', 'comment', 'pub_date')
	list_filter = ['pub_date', 'user_name']
	search_filter = ['comment']

admin.site.register(Movie)
admin.site.register(Review, ReviewAdmin)