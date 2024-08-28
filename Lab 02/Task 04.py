def Employee(name,salary=10000):
    salary_after_tax=salary-(salary*0.02)
    print(f"Name: {name}")
    print(f"Salary after tax deduction is: {salary_after_tax}")
user_input=input("Enter your name: ")
salary_input=input("Enter your salary: ")
if(salary_input):
    salary=int(salary_input)
    Employee(user_input,salary)
else:
    Employee(user_input)
        
    
    
