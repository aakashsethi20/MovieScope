import sys, os 
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviescope.settings")

import django
django.setup()

from reviews.models import Movie 


def save_movie_from_row(movie_row):
    movie = Movie()
    movie.movie_id = movie_row[0]
    movie.name = movie_row[1]
    movie.trailer_url = movie_row[2]
    movie.poster_url = movie_row[3]
    movie.date_released = movie_row[4]
    movie.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        movies_df = pd.read_csv(sys.argv[1])
        print movies_df

        movies_df.apply(
            save_movie_from_row,
            axis=1
        )

        print "There are {} movies".format(Movie.objects.count())
        
    else:
        print "Please, provide movie file path"