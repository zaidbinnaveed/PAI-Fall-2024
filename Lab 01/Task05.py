array=[]
for y in range(5):
    user_input=int(input('Enter number: '))
    array.append(user_input)
num = int(input('Enter a number such as all the numbers lessar than it be removed:'))

for y in array[:]:
    if y < num:
        array.remove(y)


print('List after removing numbers lessar than:' , num)

print(array)
