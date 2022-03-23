import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import preprocessing
from sklearn import utils
import xgboost as xgb
import matplotlib.pyplot as plt
#1. Load and Pre-Process
boston = datasets.load_boston()
data = pd.DataFrame(boston.data)
data.columns = boston.feature_names
print(data.columns)
X, y = data.iloc[:,:-1],data.iloc[:,-1]
from sklearn.model_selection import train_test_split
#2. Divide source data into Training and Test sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.15,random_state=0)
#3. Training Phase
params = {"objective":"reg:linear",'colsample_bytree': 0.3,'learning_rate': 0.1,
                'max_depth': 5, 'alpha': 10}
data_dmatrix = xgb.DMatrix(data=X,label=y)
xg_reg = xgb.train(params=params, dtrain=data_dmatrix, num_boost_round=10)
xgb.plot_tree(xg_reg,num_trees=0)
plt.rcParams['figure.figsize'] = [50, 10]
plt.show()
