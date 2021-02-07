class Student:

    def set_student(self,roll_no,course,name):
        #roll_no is local variable
        self.roll=roll_no
        self.course=course
        self.name=name
#INSTANCE VARIABLES IDENTIFIED HOW?
    #SELF IS ATTCHED TO THE VARIABLE--> self.roll

    def get_student(self):

         print(self.roll,",",self.name,",",self.course)
    # inside class, instance variables are called using self keyword

ob=Student()#using objt reference ,object call class
ob.set_student(100,"mca","reshma")
ob.get_student() #calling methods of the class using objt reference
#100 , reshma , mca

#outside class,instance variables are called using objt ref
print(ob.roll)#100

#inside class, instance variables are called using self keyword

#constructor
# duty of constructor intialise instance variable
# constructor name always class name in java  and cpp
#in python , constructor is __init__()
#constructors are invoked automatically during objt creation







