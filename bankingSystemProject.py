import sys

class Customer:
    """Customer Class with Banking Ops"""
    bankName = 'Bank of Project'

    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print('The balance after deposit is: ',self.balance)

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Funds")
            sys.exit()
        self.balance = self.balance - amount
        print('The balance after withdrawal is :',self.balance)

print("Welcome to ",Customer.bankName)
print()
name = input("Enter your name: ")
c = Customer(name)
while True:
    print('\nchoose from the given options:\n d - deposit\n w - withdraw\n e - Exit')
    option = input("Enter Your Option - ")
    if option  == 'd' or option == 'D':
        amount = float(input("Enter amount you wish to deposit: "))
        c.deposit(amount)

    elif option  == 'w' or option == 'W':
        amount = float(input("Enter amount you wish to withdraw: "))
        c.withdraw(amount)

    elif option  == 'e' or option == 'E':
        print('Thank You for Banking with Us')
        sys.exit()

    else:
        print('Invalid Option')
        

            
