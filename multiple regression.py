import pandas as pd
import numpy as np
abc = pd.read_html("https://stattrek.com/multiple-regression/regression-coefficients.aspx")
matr= abc[5] #select table
x =matr.drop('Test score',axis=1)#independent variable
y = matr['Test score'] #dependent variable
x['Student'] = 1
x_transpose = np.matrix(x).T
y_transpose = np.matrix(y).T
t = x_transpose*np.matrix(x) #multiply x trasnpose and x
inverse = np.linalg.inv(t)
coef = inverse*x_transpose*y_transpose # this return coefficient(b0,b1,b2 ....)

b0 = coef[0]
b1= coef[1]
b2 = coef[2]
print("İntercept: {} b1: {} b2: {}".format(b0,b1,b2))

predict =[b0+b1*x1+b2*x2 for x1,x2 in zip(x['IQ'],x['Study hours'])]

total = [(yi-y_pred)**2 for yi,y_pred in zip(y,predict)]
n = len(x)
mse = float(np.array(sum(total)/n))
rmse = float(mse**(1/2))
print("MSE: {} and RMSE: {}".format(mse,rmse))
