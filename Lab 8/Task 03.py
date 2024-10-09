import numpy as np

arr = np.arange(2,20,2).reshape(3,3)
mul = arr * 4
print(mul)
x = np.eye(3)
res = mul * x
print(res)
