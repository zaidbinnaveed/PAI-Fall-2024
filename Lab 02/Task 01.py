choice = int(input("What do you want to do (1 for Area of a trapezoid) (2 for Area of a parallelogram) (3 to calculate surface volume and area of a cylinder): "))
if(choice==1):
    b1=int(input("Enter base 1: "))
    b2=int(input("Enter base 2: "))
    h=int(input("Enter height: "))
    area=((b1+b2)/2)*h
    print(f"Area of trapezoid is {area}")
elif(choice==2):
    b=int(input("Enter base: "))
    h2=int(input("Enter height: "))
    area=b*h2
    print(f"Area of parallelogram is {area}")
elif(choice==3):
    r=int(input("Enter radius: "))
    h3=int(input("Enter height: "))
    area=(2*3.14*r*h3)+(2*3.14*r*r)
    volume=(2*3.14*r*h3)
    print(f"The area of cylinder is {area}")
    print(f"The volume of cylinder is {volume}")
else:
    print("Wrong choice entered!Try again.")
