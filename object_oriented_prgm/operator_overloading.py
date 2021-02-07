class Book:
    def __init__(self,pages):
        self.pages=pages

    #def __str__(self):# return only strings
        #eturn str(self.pages)
                #obj , obj1

    def __add__(self,other):#method from objt class
        return Book(self.pages+other.pages) #TypeError: unsupported operand type(s) for +: 'int' and 'Book';
        #convert to book type
                #100    +200            =300
                #300    +300            =600
    def __sub__(self, other):
        return Book(self.pages-other.pages)

    def __mul__(self, other):
        return Book(self.pages*other.pages)

    def __str__(self):
        return str(self.pages)



obj=Book(100) #typeError: __str__ returned non-string (type int)
#print(obj)
obj1=Book(200)
#print(obj1)
#type(obj)#book class
obj2=Book(300)

print(obj+obj1+obj2)#TypeError: unsupported operand type(s) for +: 'Book' and 'Book' ; + support for int and string
print(obj-obj1-obj2)
print(obj*obj1*obj2)
