import numpy as np
import pandas as pd
train = pd.read_csv('train.csv')
print ("Train data shape:", train.shape)
import matplotlib.pyplot as plt

var ='GarageArea'
data = pd.concat([train['SalePrice'], train[var]], axis=1)
plt.scatter(x=train['GarageArea'], y=train['SalePrice'])
plt.ylabel('Sale Price')
plt.xlabel('Above ground living area')
plt.show()



Q1 = data.quantile(0.35) # removing the outlets
Q3 = data.quantile(0.75)
IQR = Q3 - Q1  #training the data
print(IQR)

data_df_out = data[~((data < (Q1 - 1.5 * IQR)) |(data > (Q3 + 1.5 * IQR))).any(axis=1)]  #for plotting the data

print(data.shape)  #before removing outlets
print(data_df_out.shape)  #after removing outlets



plt.scatter(x=data_df_out['GarageArea'], y=data_df_out['SalePrice'])
plt.ylabel('Sale Price')
plt.xlabel('Above ground ')
plt.show()