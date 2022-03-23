import pandas as pd
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn import utils
from sklearn.ensemble import AdaBoostClassifier#Ensemble Learning

col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 
'bmi', 'pedigree', 'age', 'label']
# load dataset
pima = pd.read_csv("pima-indians-diabetes.csv", header=None, names=col_names)
print(pima.head())
#split dataset in features and target variable
feature_cols = ['pregnant','bmi', 'age', 'glucose', 'bp']
X = pima[feature_cols] # Features
y = pima.label # Target variable
from sklearn.model_selection import train_test_split
#2. Divide source data into Training and Test sets
X_train,X_test,y_train,y_test=train_test_split(X,y
	,test_size=0.15,random_state=0)
#3. Training Phase
# Create adaboost classifer object
clf = AdaBoostClassifier(n_estimators=1000,learning_rate=0.35)
#Train the model using the training sets
clf.fit(X_train,y_train)
# prediction on test set
y_pred=clf.predict(X_test)
#5. Measuring Accuracy
acc = accuracy_score(y_pred,y_test)#Calculate accuracy
print("Accuracy is: ", acc)