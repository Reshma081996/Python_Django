class Bamk:
    def balance_eq(self):#local method
        print("balnce")

    def withdraw(self):
        print("withdraw")

    def __deposit(self):# private method/static
        print("deposit")

class Atm(Bamk):
    pass

atm=Atm()
atm.balance_eq()
atm.withdraw()
atm._Bamk__deposit() #acessing private methods