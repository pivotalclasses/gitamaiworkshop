import statsmodels.api as sm
from sklearn import datasets
import pandas as pd
import numpy as np
#pip install stasmodels sklearn
iris = datasets.load_iris()#Load predefined dataset into Pandas dataframe
X = iris.data[:, [1,2,3]]
y = iris.target
# Apply OLS Regression for training
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model
res = np.array(predictions)
print("Predictions\n", res.astype(int))
print("Actual\n", y)
#  x1	x2	y
# 1.2	2.3	0
# 1.3	2.1	0
# 1.4 	1.8	2
# 1.1	2.1	1
# 1.4	2.2	1...1000

# y = 2.3-(1.3421*x1 + 1.1214*x2)
# Two files	->	experiment.csv(X,Y)
# 			->	live.csv(X)