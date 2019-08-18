import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('aimarks2017.csv')
# df = pd.read_csv('https://github.com/akiwelekar/MLModels/blob/master/aimarks2017.csv')
mse = df['mse']
ese = df['ese']

# Gradient-Discent Algo
n = float(len(mse))
m = 0
c = 0
lr = 0.0001
epoch = 10000
for i in range(epoch):
    ese_pred = mse*m + c
    dm = (-2/n)*sum(mse*(ese - ese_pred))
    dc = (-2/n)*sum(ese - ese_pred)
    m = m - lr*dm
    c = c - lr*dc
print('m = ', format(m, '2.3f'))
print('c = ', format(c, '2.3f'))

# sq method
mse1 = np.array(df['mse']).reshape(-1,1)
ese = np.array(df['ese']).reshape(-1,1)
rm = LinearRegression()
rm.fit(mse1, ese)
esep = rm.predict(mse1)
print('Regression Score', rm.score(mse1, esep))


plt.plot(mse1, esep, color='blue', linewidth=1, label='sq method ')
plt.plot(mse, ese_pred, color='red', linewidth=1, label='gradient discent method')
plt.scatter(mse, ese)
plt.legend()
plt.show()