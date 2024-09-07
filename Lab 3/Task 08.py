try:    
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter the second number : "))

    num3 = num1/num2
    print(num3)

except ZeroDivisionError:
    print("Error: Division by zero is not possible. Please enter a non-zero denominator.")
except ValueError:
    print("Error: Invalid input. Please enter integer values.")





