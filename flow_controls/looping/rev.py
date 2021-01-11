name="luminar"
length=len(name)-1 #length starts at 1, indexing at 0
for name in range(0,length,-1):
    print(name,end="")
reverse=""
while(length>=0):#6>=0,5>=0
    reverse+=name[length] #rev=""+name[6],rev="r"+name[5]
    length-=1#length=6-1=5,5-1=4
print(reverse)#ra