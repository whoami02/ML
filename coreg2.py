import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

marks = {
'Phy' : [15, 12, 8, 8, 7, 7, 7, 6, 5, 3],
'Hist' : [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
}
df = pd.DataFrame(marks)
p = np.array(df['Phy']).reshape(-1, 1)
h = np.array(df['Hist']).reshape(-1, 1)
rm = LinearRegression()
rm.fit(p, h)
H = rm.predict(p)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.axis(p=0.5, H=0.1)
ax.set(title='Marks', ylabel='Predicted History Marks', xlabel='Physics Marks')
ax.scatter([15, 12, 8, 8, 7, 7, 7, 6, 5, 3],
    [10, 25, 17, 11, 13, 17, 20, 13, 9, 15],
    color='red'
    
)
ax.plot(p, H, color='black', linewidth=1)

plt.show()