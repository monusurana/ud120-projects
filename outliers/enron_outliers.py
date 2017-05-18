#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus", "email_address"]

# Removing the outlier
data_dict.pop('TOTAL', 0)

data = featureFormat(data_dict, features)

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    #email = point[2]
    #print email
    matplotlib.pyplot.scatter( salary, bonus )

    # In case want to annotate to identify
    #matplotlib.pyplot.annotate(email, (salary, bonus))

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

