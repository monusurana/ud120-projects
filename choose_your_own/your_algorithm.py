#!/usr/bin/python

import matplotlib.pyplot as plt
from time import time
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

#KNN
knn = KNeighborsClassifier(n_neighbors=20)

t0 = time()
knn.fit(features_train, labels_train)
print "KNN linear training time:", round(time()-t0, 3), "s"

t1 = time()
pred = knn.predict(features_test)
print "KNN linear prediction time:", round(time()-t1, 3), "s"

accuracy = accuracy_score(pred, labels_test)
print "KNN linear accuracy:", str(round(accuracy, 3)), "%"

try:
    prettyPicture(knn, features_test, labels_test, 'knn.jpg')
except NameError:
    pass

# Adaboost
ada = AdaBoostClassifier()

t0 = time()
ada.fit(features_train, labels_train)
print "Adaboost linear training time:", round(time()-t0, 3), "s"

t1 = time()
pred = ada.predict(features_test)
print "Adaboost linear prediction time:", round(time()-t1, 3), "s"

accuracy = accuracy_score(pred, labels_test)
print "Adaboost linear accuracy:", str(round(accuracy, 3)), "%"

try:
    prettyPicture(ada, features_test, labels_test, 'adaboost.jpg')
except NameError:
    pass

# Random Forest Classifier
rfc = RandomForestClassifier(min_samples_split=20)

t0 = time()
rfc.fit(features_train, labels_train)
print "Random Forest linear training time:", round(time()-t0, 3), "s"

t1 = time()
pred = rfc.predict(features_test)
print "Random Forest linear prediction time:", round(time()-t1, 3), "s"

accuracy = accuracy_score(pred, labels_test)
print "Random Forest linear accuracy:", str(round(accuracy, 3)), "%"

try:
    prettyPicture(rfc, features_test, labels_test, 'rfc.jpg')
except NameError:
    pass