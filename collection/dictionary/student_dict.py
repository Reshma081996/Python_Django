students={"id":100,"stname":"reshma","total":250}
#print("total" in students)
if students["total"]<=250:
    print(students)
print(students["stname"])
if "course" in students:
    print("course exist")
else:
    students["course"]="ddmca"
print(students)