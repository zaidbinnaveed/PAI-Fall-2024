class Employee:
    
    def __init__(self, name, monthly_salary, percentage_tax):
        self.name = name
        self.monthly_salary = monthly_salary
        self.percentage_tax = percentage_tax
        
    def salary_after_tax(self):
        self.monthly_salary = self.monthly_salary-(self.monthly_salary * (2/100))
        return self.monthly_salary
        
    def update_tax_percentage(self, new_tax):
        self.percentage_tax = new_tax
    
    
    
    
    def employee_details(self):
        
        salary_before_tax = self.monthly_salary
        salary_after_current_tax = self.salary_after_tax()
        
        
        self.update_tax_percentage(3)
        salary_after_new_tax = self.salary_after_tax()
        
        print("Employee name : {}".format(self.name))
        print("Employee monthly salary before tax cut : {}".format(salary_before_tax))
        print("Employee salary after tax cut : {}".format(salary_after_current_tax))
        print("Employee salary after new tax cut (3%) : {}".format(salary_after_new_tax))
        print("Employee percentage tax : {}".format(self.percentage_tax))
        
p1 = Employee("Zaid", 15000, 2)
p1.employee_details()
