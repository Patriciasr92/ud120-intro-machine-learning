#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    cleaned_data = [(age, nw, (pred-nw)) for age, pred, nw in zip(ages, predictions, net_worths)]
    cleaned_data.sort(key=lambda z: z[2]**2)
    cleaned_data = cleaned_data[:-9]
    return cleaned_data
