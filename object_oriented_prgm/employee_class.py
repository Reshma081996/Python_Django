
#constructor
# duty of constructor intialise instance variable
# constructor name always class name in java  and cpp
#in python , constructor is __init__()
#constructors are invoked automatically during objt creation

class Employee:

    #def get_employee(self,id,name,designation,salary):
    def __init__(self,id,name,designation,exp,salary):#constructur is used to intialise instance variables

        self.eid=id
        self.name=name
        self.desig=designation
        self.exp=exp
        self.salary=salary


    def employee_details(self):
        print("id:",self.eid)
        print("name",self.name)
        print("designation:",self.desig)
        print("salary:",self.salary)
        print("\n")

ob=Employee(1,"reshma","engineer",25000)
#ob.get_employee(1,"reshma","engineer",25000)
ob.employee_details()
#ob1=Employee()
#ob1.get_employee(2,"resmi","developer",30000)
#ob1.employee_details()


