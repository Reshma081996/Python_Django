class Student:

    def __init__(self,roll_no,course,name,total):
        #roll_no is local variable
        self.roll=roll_no
        self.course=course
        self.name=name
        self.total=total

    def __str__(self):
        return (str(self.name))

ob1=Student(100,"django","reshma",120)
ob2=Student(101,"web","res",120)
ob3=Student(102,"django","mon",130)

slist=[]
slist.append(ob1)
slist.append(ob2)
slist.append(ob3)
total=0
for stud in slist:
    print(stud)
    if stud.course=="django":
        total+=stud.total
        print(stud.name)
print(total)



