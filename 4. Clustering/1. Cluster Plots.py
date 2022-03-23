import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
from sklearn import datasets
plt.rcParams['figure.figsize'] = (16, 9)
# Creating a sample dataset with 4 clusters
#1. Load and Pre-Process
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
from sklearn.model_selection import train_test_split
#2. Divide source data into Training and Test sets
X_train,X_test,y_train,y_test=train_test_split(iris_X,iris_y
	,test_size=0.05,random_state=0)
# Initializing KMeans
agglo = AgglomerativeClustering(n_clusters=4
	, affinity='euclidean', linkage='ward')
# Fitting with inputs
agglo.fit_predict(X_train)
# Predicting the clusters
labels = agglo.labels_
# Getting the cluster centers
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X_train[:, 0], X_train[:, 1], X_train[:, 2], c=y_train)
plt.show()