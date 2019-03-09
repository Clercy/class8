#!/usr/bin/env python

### In a script, we ran the following to find our load function

# >>> import sklearn.datasets
# >>> [func for func in dir(sklearn.datasets) if func.startswith("load")

from sklearn.datasets import load_boston
boston_data = load_boston()

dir(boston_data)
###Now, I want to list the properties of the dataset, and what they each "mean"
#TODO:
#'DESCR': this is a dataset description
# data: numpy array, in the shape rows x columns
# feature_Names: feature labels for the dataset
# target: numpy array, x rows, containing the thing we're trying to predict
# target_names: name of the class we're predicting in the categorical case

# TODO:
# 1 first, visualize your data from loading it *this way*
#  - this can actually include converting to pandas, and running your script from before
# 2 train & apply either a KNN-classifier or KNN-regressor on your dataset :)
# 3 print the output "score" or "performance" of the classifoer/regressor
# (if you did 2&3 right, your performance will *not* be perfect :) 

 
