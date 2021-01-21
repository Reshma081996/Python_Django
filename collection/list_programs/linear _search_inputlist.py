limit=int(input("enter limit"))
lst=list()
for i in range(limit):
    num=int(input("enter num "))
    lst.append(num)
print(lst)
flag=0
elt=int(input("enter element to b searched "))
ct=1
for num in lst:
    if elt==num:
        flag=flag+1
        break
    else:
        pass
    ct=ct+1
if flag==0:
    print("element not found")
else:
    print("element found at ",ct)

