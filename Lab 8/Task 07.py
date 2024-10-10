import numpy as np
numbers = [1,2,3]
arr = np.random.choice(numbers, size=1000)
print(arr)
total_sum = 0
for x in arr:
    total_sum = x + total_sum

avg = total_sum/1000
var = np.var(arr)
std = np.std(arr)
print(avg)
print(var)
print(std)
with open('zaid.txt', 'w') as file:
    file.write(f"Average: {avg}\n")
    file.write(f"Variance: {var}\n")
    file.write(f"Standard Deviation : {std}")

    
