
# coding: utf-8

# In[52]:

import sklearn
import pandas as pd
import numpy as ny
import matplotlib as mpl
from sklearn import datasets
from sklearn import linear_model
from matplotlib import pyplot
get_ipython().magic(u'cd "~\\Documents\\Assignments\\R_SAS_Data"')


# In[71]:

adult = pd.read_csv("adult.csv",  sep=",", header=False)
adult_num = adult[["Age", "fnlwgt", "education_numb", "capitol_gain", "capitol_lose", "hours_weekly"]]
adult_tar = adult[["index"]]
adult.data = pd.DataFrame.as_matrix(adult_num)
adult.target = pd.DataFrame.as_matrix(adult_tar)
adult.data[: ,0]
#adult.target


# In[41]:

X, y = adult.data, adult.target
lg = linear_model.LogisticRegression()
lg.fit(X, y)


# In[50]:

#lg.get_params(deep=True)
x = ny.array([[44, 245332, 12, 1555, 0, 30]])
lg.predict(x)
lg.predict_proba(x)


# In[74]:

pyplot.scatter(adult.data[:, 2], adult.data[:, 5])
pyplot.show()

