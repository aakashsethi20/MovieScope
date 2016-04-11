import sys, os 
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moviescope.settings")

import django
django.setup()

from reviews.models import Topic 


def save_topic_from_row(topic_row):
    topic = Topic()
    topic.topic_id = topic_row[0]
    topic.description = topic_row[1]
    topic.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        topics_df = pd.read_csv(sys.argv[1])
        print topics_df

        topics_df.apply(
            save_topic_from_row,
            axis=1
        )

        print "There are {} topics".format(Topic.objects.count())
        
    else:
        print "Please, provide topic file path"