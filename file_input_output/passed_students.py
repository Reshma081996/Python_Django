# create reference to open and read file
#lst=[]
#lst1=[]
student=set()
f=open("students","r")
for lines in f:
    word=lines.rstrip("\n")
    student.add(word)
    #lst.append(word)
#print(lst)
#student=set(lst)
print("student names : ",student)
fail=open("failed_students","r")
failed=set()
for line in fail:
    words=line.rstrip("\n")
    failed.add(words)
    #lst1.append(words)
#print(lst1)
#failed=set(lst1)
print("failed students : ",failed)

diff=student.difference(failed)
print(" passed student : ",diff)




#fail=open("failed_students","r")
#student=set((f).rstrip("\n"))
#failed_student=set(fail)
#print(student)
#for line in f:
    #print(line)
    #if line not in fail:
        #print(line)

