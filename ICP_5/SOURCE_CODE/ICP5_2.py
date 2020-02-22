import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
dataset = pd.read_csv('winequality-red.csv')

print('The total null values in the dataset are ',dataset.isnull().sum().sum())

X=dataset.drop(['quality'],axis=1)
Y=dataset[['quality']]

regr = linear_model.LinearRegression()
regr.fit(X, Y)

y_pred=regr.predict(X)

print("Variance score: %.2f" % r2_score(Y,y_pred))      # varience
print("Mean squared error: %.2f" % mean_squared_error(Y,y_pred))  #squaring errors for removing negative values
numeric_features = dataset.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print('Top 4 correlated variables to the target variable quality is: ')
print(corr['quality'].sort_values(ascending=False)[1:4],'\n')
print('Top 3 correlated variables to the target variable quality is: ')
print(corr['quality'].sort_values(ascending=False)[1:3],'\n')

