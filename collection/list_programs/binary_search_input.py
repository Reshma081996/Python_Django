limit=int(input("enter limit"))
lst=list()
for i in range(limit):
    num=int(input("enter num "))
    lst.append(num)
print(lst)
#elt=12
#step1 - sort this list
lst.sort()
print(lst)
flag=0
low=0
upp=len(lst)
element=int(input('enter num to be searched '))
while(low<=upp):
    mid=(low+upp)//2 #3
    if element>lst[mid]:
        low=mid+1

    elif(element<lst[mid]):
        upp=mid-1

    elif (element==lst[mid]):
        flag=flag+1
        break

if flag==0:
    print("element not found")
else:
    print("element  found")




#[5,6,7,8,10,11,12]
# 0               6
#l               upp



#calculate  mid=(low+upp)//2=0+6//2=3
#mid=3

#if element>lst[mid]: