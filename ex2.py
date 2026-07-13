class BankAcc:
    def __init__(self, name, bal):
        self.name = name
        self.bal = bal
        
    #Getter-Retrieve
    def ViewDetails(self):
        print(f"Name: {self.name}")
        print(f"Balance: {self.bal}")
    
    #Setter-sets new value on an attribute
    def withdraw(self, withdrawal):
        print(f"Withdrawing {withdrawal}")
        if withdrawal > self.bal:
            print("Insufficient balance!")
        else:
            self.bal-=withdrawal
            print(f"Withdraw successful.\nNew Balance: {self.bal}")
    
    def deposit(self, dep):
        print(f"Depositing {dep}")
        if dep > 0:
            self.bal+=dep
            print(f"Deposit successful.\nNew Balance: {self.bal}")
        else:
            print("Cannot deposit negative amount!")
        
payrollacc = BankAcc("Wanito Bangkalang", 1000)
print()
payrollacc.ViewDetails()
print()
payrollacc.withdraw(10)
print()
payrollacc.deposit(100)