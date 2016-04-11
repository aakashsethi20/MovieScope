import sys, os 
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviescope.settings")

import django
django.setup()

from reviews.models import MovieTopics 


def save_movietopics_from_row(movietopics_row):
    movietopics = MovieTopics()
    movietopics.movie_id = movietopics_row[0]
    movietopics.topic_id = movietopics_row[1]
    movietopics.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        movietopics_df = pd.read_csv(sys.argv[1])
        print movietopics_df

        movietopics_df.apply(
            save_movietopics_from_row,
            axis=1
        )

        print "There are {} movietopics".format(MovieTopics.objects.count())
        
    else:
        print "Please, provide movietopics file path"