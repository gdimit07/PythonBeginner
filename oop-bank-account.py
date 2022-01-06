class Account():
    
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"The deposit of {amount} has been completed.")
    
    def withdraw(self,amount):
        
        if amount > self.balance:
            print("Not enough funds.")
        else:
            self.balance = self.balance - amount
            print(f"Withdrawal of {amount} was succesfull.")

myAccount = Account("Niko", 100)
print(myAccount.balance)
myAccount.deposit(200)
print(myAccount.balance)
myAccount.withdraw(600)
print(myAccount.balance)
myAccount.withdraw(200)
print(myAccount.balance)