class BankAccount:
   
    def __init__(self, customer_name, account_number, date_of_opening, balance = 0.0):
        self.customer_name = customer_name
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount;
            print(f"Amount {amount} deposited in your bank account.")
            print(f"New balance : {self.balance}")
        else:
            print("Amount to be deposited must be positive.")
            
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Cannot complete transaction.")
        elif amount <= 0:
            print("Amount to be withdrawn must be positive.")
        else:
            self.balance = self.balance - amount
            print(f" Amount {amount} withdrawn from bank account.\n")
            print(f"Remaining balance : {self.balance}")
    
    def check_balance(self):
        print(f"Amount remaining in your bank account : {self.balance}")
        
    def customer_details(self):
        print("Customer name : ", self.customer_name)
        print("Customer account number : ", self.account_number)
        print("Balance in account : ", self.balance)
        print("Date of Opening of Account : ", self.date_of_opening)
        
p1 = BankAccount("Zaid", 12345, "24 February", 15000)
p1.customer_details()
print("\nWelcome to Bank Management System!")
print("1. Deposit money")
print("2. Withraw money")
print("3. Check Balance")
choice = int(input("Enter your choice : "))

if choice == 1:
    amount = float(input("Enter the amount to deposit: "))
    p1.deposit(amount)
elif choice == 2:
    amount = float(input("Enter the amount to withdraw: "))
    p1.withdraw(amount)
elif choice == 3:
    p1.check_balance()
else:
    print("Invalid choice entered. Please try again.")
    
       
