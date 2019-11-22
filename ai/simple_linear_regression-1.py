import numpy as np
from sklearn.linear_model import LinearRegression

#  regressor
x = np.array([5, 15, 25, 35, 45, 55])
print(f'The array is:{x}')

x_transformed = x.reshape(-1, 1)
# print(f'The array is:{x_transformed}')

x = x_transformed
print(f'The Regressor is:\n{x}')

#  predictor/regressand
y = np.array([5, 20, 14, 32, 22, 38])
print(f'The predictor is:{y}')

#  model building
model = LinearRegression()
model.fit(x, y)
print(f'Model Structure:{model}')

#  Same as line #19 & line #20 model = LinearRegression().fit(x,y)

# Co-efficient of determination
r_sqr = model.score(x, y)
print(f'Co-efficient of determination:{r_sqr}')

# Prediction
y_pred = model.predict(x)
print(f'Prediction:{y_pred}')
print(f'The predictor is:{y}')


#  Intercept
print(f'Intercept:{model.intercept_}')

#  Slope: coefficient of x
print(f'Slope:{model.coef_}')
