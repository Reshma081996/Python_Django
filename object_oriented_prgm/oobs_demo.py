#create class Person and print this age name

class Person: # capital letter
    #methods
    def setPerson(self,age,name): #here age, name are local variable
        self.age=age # self.name, self.age are instance variables
        self.name=name
    def print_data(self):
        print("name : ",self.name)
        print("age: ",self.age)

obj=Person() # using reference obj ,connecting objt and class
obj.setPerson("25","reshma")
obj.print_data()
