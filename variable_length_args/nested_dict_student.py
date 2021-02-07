#print_data(roll=1000), print name of student
#print_data(roll=1001), propertty="course" ##name,course

f=open("student_demo","r")

students={}

for line  in f:
   id,name,total,course=line.rstrip("\n").split(",")
   #print(id,name,total,course)
   if id not in students:
      students[id]={"id":id,"name":name,"total":total,"course":course}
   #print(students)
def print_data(**kwargs):
   #print(kwargs)
   id=kwargs["id"]
   if id in students:
      print(students[id]["name"])
      if "prop" in kwargs:
         pro=kwargs["prop"]
         print(students[id][pro])
      else:
         print("student with id doesnt exist")
print_data(id="1000",prop="course")





