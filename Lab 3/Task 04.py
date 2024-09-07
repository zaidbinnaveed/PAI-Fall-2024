with open('zaid.txt', 'w') as file:
    name = input('Enter name : ')
    age = input('Enter age : ')
    cnic = input("Enter CNIC no. : ")
    salary = input("Enter salary : ")
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Cnic: {cnic}\n")
    file.write(f"Salary: {salary}\n")

with open('zaid.txt', 'a') as file:
    contact_number = input("Enter your contact info : ")
    file.write(f"Contact_number: {contact_number}\n")

with open('zaid.txt' ,'r') as file:
    content = file.read()
print(content)
