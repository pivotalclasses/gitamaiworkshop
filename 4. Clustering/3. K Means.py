import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
# Load datasets
train_url = "train.csv"
train = pd.read_csv(train_url)
# Remove unnecessary Columns
train = train.drop(['PassengerId','Name','Ticket', 'Cabin','Embarked'], axis=1)
# Encoding Labels
labelEncoder = LabelEncoder()
labelEncoder.fit(train['Sex'])
train['Sex'] = labelEncoder.transform(train['Sex'])
# Fill missing values with mean column values in the train set
train.fillna(train.mean(), inplace=True)
# Specify Model
X = np.array(train.drop(['Survived'], 1).astype(float))
y = np.array(train['Survived'])
X_train,X_test,y_train,y_test=train_test_split(X,y
	,test_size=0.25,random_state=0)
# Implement K-Means Clustering
kmeans = KMeans(n_clusters=1) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(X_train,y_train)
# prediction on test set
y_pred=kmeans.predict(X_test)
#5.Measuring Accuracy
acc = accuracy_score(y_pred,y_test)#Calculate accuracy
print("Accuracy is: ", acc)