# Required Packages
from sklearn import datasets		# To Get iris dataset
from sklearn import svm    			# To fit the svm classifier
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
X = iris.data[:, 0:4]  # we only take the Sepal two features.
y = iris.target
C = 1.0  #SVM regularization parameter
# SVC with linear kernel
svc_pred_y = svm.SVC(kernel='linear', C=C).fit(X, y).predict(X)
svc_acc = accuracy_score(svc_pred_y,y)#Calculate accuracy
print("Linear Accuracy is: ", svc_acc)
# LinearSVC (linear kernel)
lin_svc_pred_y = svm.LinearSVC(C=C).fit(X, y).predict(X)
lin_svc_acc = accuracy_score(lin_svc_pred_y,y)#Calculate accuracy
print("SVC LinearAccuracy is: ", lin_svc_acc)
# SVC with RBF kernel
rbf_svc_pred_y = svm.SVC(kernel='rbf', gamma=0.75, C=C).fit(X, y).predict(X)
rbf_svc_acc = accuracy_score(rbf_svc_pred_y,y)#Calculate accuracy
print("SVC RBF Accuracy is: ", rbf_svc_acc)
# SVC with polynomial (degree 3) kernel
poly_svc_pred_y = svm.SVC(kernel='poly', degree=6, C=C).fit(X, y).predict(X)
poly_svc_acc = accuracy_score(poly_svc_pred_y,y)#Calculate accuracy
print("SVC Polynomial Accuracy is: ", poly_svc_acc)
