import sys, os 
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviescope.settings")

import django
django.setup()

from reviews.models import Actor 


def save_actor_from_row(actor_row):
    actor = Actor()
    actor.actor_id = actor_row[0]
    actor.first_name = actor_row[1]
    actor.last_name = actor_row[2]
    actor.date_of_birth = actor_row[3]
    actor.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        actors_df = pd.read_csv(sys.argv[1])
        print actors_df

        actors_df.apply(
            save_actor_from_row,
            axis=1
        )

        print "There are {} actors".format(Actor.objects.count())
        
    else:
        print "Please, provide actor file path"