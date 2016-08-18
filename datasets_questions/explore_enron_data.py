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

import math

# print(len([p for p in enron_data if enron_data[p]['poi'] == 1]
# print(enron_data.keys())
# print(enron_data['PRENTICE JAMES'])
# print(enron_data['COLWELL WESLEY'])
# print(enron_data['SKILLING JEFFREY K'])
print(enron_data['LAY KENNETH L'])
print(enron_data['FASTOW ANDREW S'])
print(len([p for p in enron_data if enron_data[p]['salary'] != 'NaN']))
print(len([p for p in enron_data if enron_data[p]['email_address'] != 'NaN']))
print(len([p for p in enron_data if enron_data[p]['total_payments'] == 'NaN']))
print(len([p for p in enron_data if enron_data[p]['total_payments'] == 'NaN' and enron_data[p]['poi']]))
print(len([p for p in enron_data if enron_data[p]['poi']]))
print(len(enron_data))
