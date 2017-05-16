#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "No of people in the data set:", len(enron_data)
print "No of features in each data set:", len(enron_data['METTS MARK'])

poi_count = 0
salary_count = 0
email_count = 0
total_payment_nan_count = 0
total_payment_nan_poi_count = 0

for key in enron_data:
    if enron_data[key]['poi']:
        poi_count = poi_count + 1

    if enron_data[key]['salary'] != 'NaN':
        salary_count = salary_count + 1

    if enron_data[key]['email_address'] != 'NaN':
        email_count = email_count + 1

    if enron_data[key]['total_payments'] == 'NaN':
        total_payment_nan_count = total_payment_nan_count + 1

    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi']:
        total_payment_nan_poi_count = total_payment_nan_poi_count + 1

print "POI Count:", poi_count
print "People with salary mentioned:", salary_count
print "People with email mentioned:", email_count
print "People with total payments missing:", total_payment_nan_count, "percentage:", float(total_payment_nan_count)/len(enron_data)
print "POI with total payments missing:", total_payment_nan_poi_count, "percentage:", float(total_payment_nan_poi_count) / poi_count

print "James Prentice Total Stock value:", enron_data['PRENTICE JAMES']['total_stock_value']
print "Wesley Colwell Emails to POI:", enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print "Jeffrey K Skilling Stock options exercised:", enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print "Total Payments: Skillings:", enron_data['SKILLING JEFFREY K']['total_payments'], "Lay:", enron_data['LAY KENNETH L']['total_payments'], "Fastow:", enron_data['FASTOW ANDREW S']['total_payments']