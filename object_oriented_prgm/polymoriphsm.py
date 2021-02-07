
#polymorphism - more than one forms
#method overloading
#method overriding - inheritance
#operator overloading

#method overloading- same method with different no of arguemnets
#method ovrlaoding not supported in python
#python consider recently implemented constructor onlyyy
class Maths:
    def add(self):
        print("no arguements")

    def add(self,num1):
        print("1 arguements")
    def add(self,num1,num2):
        print("2 arguements")

obj=Maths()

obj.add(1,2)
obj.add(10) ##python consider recently implemented constructor onlyyy


