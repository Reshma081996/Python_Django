class Parent:
    def m1(self):
        print("inside parent1")

class Child(Parent):
    def m2(self):
        print("inside child")

class Subchild(Child):
    def m3(self):
        print("inside subchild")

obj=Subchild()#EATE REFERENCE FOR SUBCLASS
obj.m3()
obj.m2()
obj.m1()

# subchild inherits->child->parent=== multilevel inheritance