import numpy as np
from scipy import stats

a = []
n = int(input())
for i in range(0, n, 1):
    x = int(input())
    a.append(x)
array = np.array(a, dtype = np.int64)
mean = np.mean(a)
median = np.median(a, axis = None, out=None)
mode = stats.mode(a)
l = mean - 1.96*(array.std()/(n**(1/2)))
u = mean + 1.96*(array.std()/(n**(1/2)))
print(mean)
print(median)
print(mode)
# print(array.std())
print(format(array.std(), '6.2f'))
lb = format(l, '6.1f')
ub = format(u, '6.1f')
print(lb, ub)