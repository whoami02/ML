import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = {
'Phy' : [15, 12, 8, 8, 7, 7, 7, 6, 5, 3],
'Hist' : [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
}
df = pd.DataFrame(marks)
px = df['Phy'].mean()
hx = df['Hist'].mean()
psd = df['Phy'].std()
hsd = df['Hist'].std()
cov = df['Phy'].cov(df['Hist'])
# Karl-Pearson Coefficient
r = cov/(psd*hsd)
print('Karl-Pearson Coeff. = ', format(r, '0.3f'))
# value of Slope
B1 = r*(psd/hsd)
print('Value of Slope = ', format(B1, '0.3f'))

B0 = hx - (B1*px)

#predicting history marks if marks in phy = 10 
H1 = B0 +B1*10
print('Predicted marks in History = ', format(H1, '2.3f'))
