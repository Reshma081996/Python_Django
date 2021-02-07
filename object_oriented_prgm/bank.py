#withdrawal,deposit,balance,create account

from datetime import  datetime

class Bank:

    bank_name= "sbi"  # static variables or class varaibles and acessesd using class.variable
    #def create_account(self,acc_no,name,mini_balance): #intialises instance variables
    def __init__(self,acc_no,name,mini_balance):
        self.accno=acc_no
        self.p_name=name
        self.balance=mini_balance
        #self.bank=bank

    def deposit(self,amount):
        self.balance+=amount
        print(Bank.bank_name,"account no",self.accno,"is deposited with",amount,"on",datetime.today(),"Available balance is",self.balance)
        #class variable is acessesd using class.variable
    def withdrawal(self,amount):
        if self.balance>amount:
            self.balance-=amount
            print("your account no", self.accno, "is credited with", amount, "on", datetime.today(), "Available balance is",self.balance)
        else:
            print("Dont have sufficient balance to withdraw")

    def balance_enquiry(self):
        print(self.balance)


obj=Bank(1000,"resham",3000)# constructor are automatically ivoked during objt creation
#obj=Bank()
#obj.create_account(1000,"resham",3000)
obj.deposit(1000000)

obj.withdrawal(250)

obj.balance_enquiry()
