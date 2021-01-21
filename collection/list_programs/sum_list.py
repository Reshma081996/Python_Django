limit=int(input("enter limit"))
lst=list()
lst1=list()

for i in range(limit):
    num = int(input("enter num"))
    lst.append(num)
print(lst)

total=sum(lst)
print(total)
for i in lst:
    res=total-i
    lst1.append(res)
print(lst1)

