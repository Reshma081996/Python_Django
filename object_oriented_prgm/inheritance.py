#inheritance - child inherit the properties of parent class

#object class is base class for every class
class Parent(object):
    def phone(self):
        print("i have iphone")

    def __str__(self): #method of class object - parent overrides that method from object class
        return"hello" #__str return only strings

class Child(Parent):
    pass

#num=int("23")
#print(type(num))#<class 'int'>
c=Child()
#print(type(c))#<class '__main__.Child'>
print(c)#<__main__.Child object at 0x000002321FBF8400>
#while printing objt reference, __str__() will b invoked