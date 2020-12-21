#--------------------------SIMPLE LINEAR REGRESSION-----------------------------
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
x = pd.DataFrame([2,12,5,10,0])
y = pd.DataFrame([30,65,50,80,10])
reg = LinearRegression()
model = reg.fit(x,y)
a =  model.intercept_
b = model.coef_
# print('model inter:',a)
# print('model_coef:',b)
# print('Model Scro:',c)
a = (x*y).sum()
b = (x**2).sum()
X_ort = x.mean()
Y_ort = y.mean()
b1 = (a-(5*X_ort*Y_ort))/(b-(5*(X_ort**2))) # b1 katsayısını bulduk coef_ değerini bulduk.
intercept = Y_ort-(b1*X_ort)
# y'nin ortalamasından b çarpı x'in ortalamaınıs çıkartırız.
# print(round(b1,3))
tahmin = int(input('Tahmin girin:'))
y2 = intercept+(b1*tahmin)
modeltah = model.predict([[tahmin]])
print('Model Tahmin:',modeltah)
# mse = mean_squared_error(y,model.predict(x))
print('My_predict:',y2)
# Mean_squared_error = np.mean(((y-y2)**2))
# print('Model MSE:',mse)
# print('My_MSE:',Mean_squared_error)













#--------------------------SİMPLE LİNEAR REGRESSİON--------------------------------------
# x = pd.DataFrame([2,12,5,10,0])
# y = pd.DataFrame([30,65,50,80,10])
# a = (x*y).sum()
# b = (x**2).sum()
# X_mean = x.mean()
# Y_mean = y.mean()
# b1 = (a-(5*X_mean*Y_mean))/(b-(5*(X_mean**2))) # b1 values is coef_
# intercept = Y_mean-(b1*X_mean) # b0 values
# # predict = int(input('Login values for predict:'))
# predict = intercept+(b1*x)
# print('İntercept:',intercept)
# print('Coef:',b1)
# print('Predict:',predict)
#
# mean_squared_error = np.mean(((y-predict)**2))
# print('MSE:',mean_squared_error)
# sqr_squared_mean_error = np.sqrt(mean_squared_error)
# print('RMSE:',sqr_squared_mean_error)





# import pandas as pd
# import numpy as np
# x = pd.DataFrame([2,12,5,10,0])
# y = pd.DataFrame([30,65,50,80,10])
# a = (x*y).sum()
# b = (x**2).sum()
# X_ort = x.mean()
# Y_ort = y.mean()
# b1 = (a-(5*X_ort*Y_ort))/(b-(5*(X_ort**2))) # b1 katsayısını bulduk
# intercept = round(Y_ort-(b1*X_ort),2)
# # y'nin ortalamasından b çarpı x'in ortalamaınıs çıkartırız.
# print(round(b1,3))
# print('İntercept:',intercept)





#  city = []
# i = 0
# while i<3:
#     a = input("Login City:")
#     city.append(a)
#     i+=1
# print(city)






# a = str(11111111111111111111)
# liste = []
# for i in a:
#     b = int(i)
#     liste.append(b)
#     print(liste)
# print(sum(liste))
