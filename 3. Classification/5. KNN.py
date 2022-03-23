import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
#1. Load and Pre-Process
df = sns.load_dataset('iris')
data = df[['sepal_length','sepal_width','petal_length','petal_width']]
target = df['species']#Select Target Column
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
test_data = [[1.2, 2.3, 1.3, 3.1],[1.4, 1.3, 2.1, 3.6],[3.1, 2.2, 2.1, 2.3]]#Define input test data
prediction = knn.predict(test_data)#Send test data to predict function
print(prediction)#Show Predictions