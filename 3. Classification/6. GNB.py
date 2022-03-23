from sklearn import datasets
iris = datasets.load_iris()
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
gnb = GaussianNB()
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
acc = accuracy_score(y_pred,iris.target)#Calculate accuracy
print("Accuracy is: ", acc)