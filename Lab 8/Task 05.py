import numpy as np

numbers = [2,5,9,10]

arr = np.random.choice(numbers, size=(4,4))
print(arr)
x = np.eye(4)
res = arr * x
print(res)
arr1 = np.arange(1,32,2).reshape(4,4)
res2 = res * arr1
print(res2)
