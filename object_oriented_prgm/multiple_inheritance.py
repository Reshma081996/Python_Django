class Parent:
    def m1(self):
        print("inside parent 1")
    def m2(self):
        print("hallo")

class Child:
    def m1(self):
        print("inside child 1")


class Subclass(Child,Parent):#inside child 1-(based on given class-child is given first)
    def m3(self):
        print("inside subc")

obj=Subclass()
obj.m1()
obj.m2()