import pandas as pd
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn import utils
from sklearn.ensemble import AdaBoostClassifier#Ensemble Learning
#1. Load and Pre-Process
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
from sklearn.model_selection import train_test_split
#2. Divide source data into Training and Test sets
X_train,X_test,y_train,y_test=train_test_split(iris_X,iris_y
	,test_size=0.15,random_state=0)
#3. Training Phase
# Create adaboost classifer object
clf = AdaBoostClassifier(n_estimators=50,learning_rate=1)
#Train the model using the training sets
clf.fit(X_train,y_train)
# prediction on test set
y_pred=clf.predict(X_test)
#5. Measuring Accuracy
acc = accuracy_score(y_pred,y_test)#Calculate accuracy
print("Accuracy is: ", acc)