array=[]
count=0
for y in range(10):
    user_input=int(input('Enter number: '))
    array.append(user_input)
    if user_input % 2 == 0:
        count=count+1
print('Number of even numbers in the list: ',count)
