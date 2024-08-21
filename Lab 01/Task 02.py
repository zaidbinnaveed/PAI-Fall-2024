var1 = int(input('Enter your first value: '))
var2 = int(input('Enter your second value: '))
choice = str(input('What do you want to do (+,-,/,*) :'))


if choice == "+":
    result = var1-(-var2)
    print('Result:',result)
elif choice == "-":
    result = var1 - var2
    print('Result:', result)
elif choice == "*":
    result = var1 * var2
    print('Result:',result)
elif choice == "/":
    result = var1/var2
    print('Result:',result)
else:
    print("Wrong choice entered! Try again.")
