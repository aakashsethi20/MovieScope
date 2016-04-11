import sys, os 
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviescope.settings")

import django
django.setup()

from reviews.models import ActorPlays 


def save_actorplays_from_row(actorplays_row):
    actorplays = ActorPlays()
    actorplays.actor_id = actorplays_row[0]
    actorplays.movie_id = actorplays_row[1]
    actorplays.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        actorplays_df = pd.read_csv(sys.argv[1])
        print actorplays_df

        actorplays_df.apply(
            save_actorplays_from_row,
            axis=1
        )

        print "There are {} actorplayss".format(ActorPlays.objects.count())
        
    else:
        print "Please, provide actorplays file path"