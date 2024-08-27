num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your first number:"))
num3 = int(input("Enter your first number:"))
if(num1==num2 and num2==num3):
    print("All numbers are the same")
elif(num1>num2 and num1>num3):
    print(f"{num1} is greatest number")
elif(num2>num1 and num2>num3):
    print(f"{num2} is the greatest number")
elif(num3>num2 and num3>num1):
    print(f"{num3} is the greatest number")
