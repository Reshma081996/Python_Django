#print employee deails whose designation developrt
#no f emplyees as developer
#print employee details who  ahve highest ,min salary
#
class Employee:

    #def get_employee(self,id,name,designation,salary):
    def __init__(self,eid,name,designation,exp,salary):#constructur is used to intialise instance variables

        self.eid=eid
        self.name=name
        self.desig=designation
        self.exp=exp
        self.salary=salary

    def __str__(self):
        return self.name

f=open("employee","r")
emplist=[]
for line in f:
    #print(line)
    #1000,anoop,developer,2,25000\n
    eid,name,desig,exp,salary=line.rstrip("\n").split(",")
    emplist.append(Employee(eid,name,desig,exp,salary))


for employee in emplist:
    print(employee)
    #if employee.desig=="developer":
        #print(employee.name)

# name of developers
desig_name=list(filter(lambda emp:emp.desig=="developer",emplist))
#print(desig_name)
#print(len(desig_name))
for emp in desig_name:
    print(emp)

#no of employees ad developer

cnt=len(list(filter(lambda emp:emp.desig=="developer",emplist)))
print(cnt)


max_sal=max(list(map(lambda emp:emp.salary,emplist)))
print(max_sal)

min_sal=min(list(map(lambda emp:emp.salary,emplist)))
print(min_sal)


#sal=[]
#for employee in emplist:
    #sal.append(employee.salary)

    #highvalue=max(sal)
    #minvalue=min(sal)
#print(highvalue)
#print(minvalue)

#for employee in emplist:
    #if employee.salary==highvalue:
        #print("employee having high salary ",employee.name)

#for employee in emplist:
    #if employee.salary==minvalue:
        #print("employee having low salary ",employee.name)

#developer with min salary
#develop=[]
#for employee in emplist:
    #if employee.desig=="developer":
        #develop.append(employee.salary)
#print(develop)

#for employee in emplist:
    #low=min(develop)
    #if employee.salary==low:
        #print(employee.name,"having",low)
#print(low)
