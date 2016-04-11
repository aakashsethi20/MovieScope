import sys, os 
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviescope.settings")

import django
django.setup()

from reviews.models import Directs 


def save_directs_from_row(directs_row):
    directs = Directs()
    directs.director_id = directs_row[0]
    directs.movie_id = directs_row[1]
    directs.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        directs_df = pd.read_csv(sys.argv[1])
        print directs_df

        directs_df.apply(
            save_directs_from_row,
            axis=1
        )

        print "There are {} directs".format(Directs.objects.count())
        
    else:
        print "Please, provide directs file path"