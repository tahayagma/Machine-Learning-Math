#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn import neighbors

from warnings import filterwarnings
filterwarnings('ignore')

df = pd.read_csv(r"C:\Users\tahay\Desktop\UDEMY\(2020) Python ile Makine Öğrenmesi(Machine Learning)\Bölüm 7 Linear Regression Models (Doğrusal Regresyon Modelleri)\Hitters.csv")
df.dropna(inplace=True)
dms = pd.get_dummies(df[['League','Division','NewLeague']])
y = df["Salary"]
X_ =df.drop(['Salary','League','Division','NewLeague'],axis=1).astype('float64')
X = pd.concat([X_,dms[['League_N','Division_W','NewLeague_N']]],axis=1)

X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.25,random_state=1)

X_train.head()

knn_model = KNeighborsRegressor().fit(X_train,y_train)

dir(knn_model)

knn_model

knn_model.n_neighbors

knn_model.metric

y_pred = knn_model.predict(X_test)[0:5]
# tahmin işleminde X_test verisini kullandığımız için bizim
#gerçek değerlerimiz y_test grubu olur

y_pred

np.sqrt(mean_squared_error(y_test[0:5],y_pred))
#tahmin etme işlemini X_testinin ilk 5 gözlemi için yaptığımdan dolayı gerçek değerlerden de ilk 5 gözlemi seçmek lazım
# tahmin işelmini gerçekleşmesi için


# # KNN Euclidean matematiksel algoritma 

X = pd.DataFrame({'X1':[56,85,25,56,80,90,40],
                   'X2':[241,250,233,231,220,200,225]})

Y = pd.DataFrame({'Y': [100,120,150,140,150,135,130]})
pred_x = pd.DataFrame({'a1':[50],'b1':[230]})

knn_model= KNeighborsRegressor(n_neighbors=3,metric='euclidean').fit(X,Y)

knn_model.predict([[100,130]])

x1_a1= []
for i in X['X1']:
    for j in pred_x['a1']:
        x1_a1.append((j-i)**2)
x1_a1 = pd.DataFrame(x1_a1)

x2_b1= []
for i in X['X2']:
    for j in pred_x['b1']:
        x2_b1.append((j-i)**2)
x2_b1 = pd.DataFrame(x2_b1)

sn = pd.concat([x1_a1,x2_b1],axis= 1)
sn.columns = ['x1-yi','x2-yi']
sn['total'] = sn['x1-yi']+sn['x2-yi']
sn['sqrt']=np.sqrt(sn['total'])
sn
#sqrt is distance values

k =int(input('Login K value:'))
a =sn.nsmallest(n=k,columns='sqrt').index
predict_Y =np.sum(Y.iloc[a])/k
predict_Y

