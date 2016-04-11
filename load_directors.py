import sys, os 
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviescope.settings")

import django
django.setup()

from reviews.models import Director 


def save_director_from_row(director_row):
    director = Director()
    director.director_id = director_row[0]
    director.first_name = director_row[1]
    director.last_name = director_row[2]
    director.country = director_row[3]
    director.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        director_df = pd.read_csv(sys.argv[1])
        print director_df

        director_df.apply(
            save_director_from_row,
            axis=1
        )

        print "There are {} director".format(Director.objects.count())
        
    else:
        print "Please, provide director file path"