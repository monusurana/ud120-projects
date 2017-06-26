#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
from sklearn import tree
from sklearn import model_selection
import numpy as np
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

clf = tree.DecisionTreeClassifier()

clf.fit(features, labels)
print "DT linear accuracy before CV:", clf.score(features, labels)

features_train, features_test, labels_train, labels_test = model_selection.train_test_split(features, labels, test_size=0.3, random_state=42)

clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score,precision_score,recall_score
accuracy = accuracy_score(pred, labels_test)
precision = precision_score(pred, labels_test)
recall = recall_score(pred, labels_test)

pois = np.array(labels_test)
pois_count = np.count_nonzero( pois == 1.0)
pois_total = len(labels_test)
print "No of POIs in test set:", pois_count
print "No of people in test set:", pois_total
print "Accuracy if identifier predicted 0:", float(pois_total - pois_count)/pois_total

print "Prediction array:", np.array(pred)
print "Labels array:", np.array(labels_test)

print "DT accuracy after CV:", str(round(accuracy, 3)), "%"
print "DT precision after CV:", str(round(precision, 3)), "%"
print "DT recall after CV:", str(round(recall, 3)), "%"

# Question
# predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
# true labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]