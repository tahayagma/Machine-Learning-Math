# __author__:@freedom.code
# The basic math behind simple linear regression

import pandas as pd
import numpy as np

x = pd.DataFrame([2,12,5,10,0])
y = pd.DataFrame([30,65,50,80,10])
a = (x*y).sum()
b = (x**2).sum()
X_mean = x.mean()
Y_mean = y.mean()
b1 = (a-(5*X_mean*Y_mean))/(b-(5*(X_mean**2))) # b1 values is coef_
intercept = Y_mean-(b1*X_mean) # b0 values
# predict = int(input('Login values for predict:'))
predict = intercept+(b1*x)
print('İntercept:',intercept)
print('Coef:',b1)
print('Predict:',predict)

mean_squared_error = np.mean(((y-predict)**2))
print('MSE:',mean_squared_error)
sqr_squared_mean_error = np.sqrt(mean_squared_error)
print('RMSE:',sqr_squared_mean_error)




