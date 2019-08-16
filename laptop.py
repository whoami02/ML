import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt')
# data = pd.read_csv('trainingdata.txt')
data.columns = ['1', '2']
mean1 = data['1'].mean()
mean2 = data['2'].mean()
std1 = data['1'].std()
std2 = data['2'].std()

cov = data['1'].cov(data['2'])      #co-variance

r = cov/(std1*std2)     #Karl-Pearson Coeff
slope = r*(std2/std1)        
c = mean2 - (slope*mean1)

x = float(input())
y = slope*x + c
print(format(y, '4.2f'))