employe={"id":100,"ename":"ajay","exp":2,"salary":35000}
#print("salary"in employe)
if "salary" in employe:
    print(employe["salary"])
print(employe["ename"])

if "gender" in employe:
    print("gender exists")
else:
    employe["gender"]="male"
print(employe)

if employe["salary"]<=35000:
    employe["salary"]+=5000
    print(employe)

