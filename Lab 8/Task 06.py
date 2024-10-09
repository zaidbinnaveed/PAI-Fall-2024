import numpy as np

numbers = [1,2,3,4,5]
arr = np.random.choice(numbers, size = (5,3))
print(arr)
numbers1 = [6,7,8,9]
arr1 = np.random.choice(numbers1, size = (3,2))
print(arr1)
res = np.dot(arr,arr1)
print(res)
