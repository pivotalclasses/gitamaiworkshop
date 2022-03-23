import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
#1. Load and Pre-Process
dt = pd.read_csv('studk-pred.csv')#Load Dataset
data = dt.drop(['stu_id','type'],axis=1)#Remove unnecessary columns
target = dt['type']#Select Target Column
from sklearn.model_selection import train_test_split
#2. Divide source data into Training and Test sets
X_train,X_test,y_train,y_test=train_test_split(data,target
	,test_size=0.2,random_state=0)
#3. Training Phase
knn = KNeighborsClassifier(n_neighbors=5)#Define k-value
knn.fit(X_train, y_train)#Send Data, Target to Fitness function
#4. Testing Phase
pred_y = knn.predict(X_test)#Do a test prediction on actual train data
#5. Measuring Accuracy
acc = accuracy_score(pred_y,y_test)#Calculate accuracy
print("Accuracy is: ", acc)
#6. Working with Future Data for Forecast
test_data = [[56,45,34,78],[89,78,44,48],[98,44,45,87]]#Define input test data
prediction = knn.predict(test_data)#Send test data to predict function
print(prediction)#Show Predictions