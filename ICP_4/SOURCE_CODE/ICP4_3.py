import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
train_df = pd.read_csv('./glass.csv')
X_train = train_df.drop("Type",axis=1)
Y_train = train_df["Type"]


X_train, X_test, Y_train, y_test= train_test_split(X_train, Y_train, test_size=0.2, random_state=0)
print(train_df[train_df.isnull().any(axis=1)])
##SVM
svc = SVC()
svc.fit(X_train, Y_train)
Y_pred = svc.predict(X_test)
acc_svc = round(svc.score(X_train, Y_train) * 100, 2)
print("svm accuracy is:", acc_svc)