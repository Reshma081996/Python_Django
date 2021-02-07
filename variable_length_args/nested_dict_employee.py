employee={
    1000:{"id":1000,"name":"tom","salary":25000,"exp":1},
    1001:{"id":1001,"name":"jhon","salary":30000,"exp":2},
    1002:{"id":1002,"name":"danie","salary":35000,"exp":2},
    1003:{"id":1003,"name":"jack","salary":30000,"exp":2}
}
# nested dictionary
#if 1000 in employee: # key 1000 values
    #print(employee[1000]) # check for key 1000 in employees
    #{'id': 1000, 'name': 'tom', 'salary': 25000, 'exp': 1}


#print name of employee id =1001
if 1001 in employee:
    print(employee[1001]["name"])
else:
    print("employee with this id does not exist")

#salary of id =1003
if 1001 in employee:
    print(employee[1001]["salary"])
else:
    print("employee with this id does not exist")

#create a method and it will print corresponding employee name
def print_employ(**kwargs):
    #print(kwargs) #{'id': 1002, 'prop': 'salary'}
    if id in employee:
        print(employee[id]["name"])
    else:
        print("#employee with this id does not exist")
#print_employ(id=1002)
print_employ(id=1002,prop="salary")

#create a method
def print_employee(**kwargs):

        #print(kwargs) #{'id': 1000, 'prop': 'salary'}
        id=kwargs["id"]# id =kwarg['id']
        if id in employee:
            print(employee[id]["name"])
            if "prop" in kwargs:
                salary=kwargs["prop"]
                print(employee[id][salary])
            else:
                pass
        else:
            print("employee with this id does not exist")
print_employee(id=1000,prop="salary")