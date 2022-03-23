# import statements
from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt
# import KMeans
# import hierarchical clustering libraries
import scipy.cluster.hierarchy as sch
# create blobs
data = make_blobs(n_samples=200, n_features=2, centers=4, 
	cluster_std=1.6, random_state=50)
# create np array for data points
points = data[0]
# create dendrogram
dendrogram = sch.dendrogram(sch.linkage(points, method='ward'))
plt.show()