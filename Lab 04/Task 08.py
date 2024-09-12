class Account :
    
    def __init__(self):
        self.account_no = None
        self.account_bal = None
        self.security_code = None
        
        
    def initialise(self,account_no, account_balance, security_code):
        self._account_no = account_no
        self._account_balance = account_balance
        self._security_code = security_code
        
    def account_details(self):
        print(f"Account number : {self._account_no}")
        print(f"Account balance : {self._account_balance}")
        print(f"Security code : {self._security_code}")
        
my_account = Account()
my_account.initialise(123456, 50000, 7227)
my_account.account_details()
