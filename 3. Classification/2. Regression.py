from sklearn import linear_model
import numpy as np
import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
np.random.seed(0)#Shuffle
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-100]]
iris_y_train = iris_y[indices[:-100]]
# Note the difference in argument order
lm = linear_model.LinearRegression()
model = lm.fit(iris_X_train,iris_y_train)
pred_y = lm.predict(iris_X_train) #Do Prediction
test_y = iris_y_train#Select Target Column
print("Actual Data: ", test_y[0:10])
print("Predicted Data: ", pred_y[0:10].astype(int))
