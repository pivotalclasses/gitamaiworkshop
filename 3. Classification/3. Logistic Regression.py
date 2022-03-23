import pandas as pd
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 
'bmi', 'pedigree', 'age', 'label']
# load dataset
pima = pd.read_csv("pima-indians-diabetes.csv", header=None, names=col_names)
print(pima.head())
#split dataset in features and target variable
feature_cols = ['bmi', 'age','glucose','bp']
X = pima[feature_cols] # Features
y = pima.label # Target variable
# split X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,
	random_state=0)
# import the class
from sklearn.linear_model import LogisticRegression
# instantiate the model (using the default parameters)
logreg = LogisticRegression(max_iter=10000,solver='lbfgs')
# fit the model with data
logreg.fit(X_train,y_train)
# do prediction
y_pred=logreg.predict(X_test)
print(y_test[0:15])
print(y_pred[0:15])