lst=[10,11,12,13,14,15]

elt=int(input("enter element to be searched"))
flag=0
count=1
for num in lst:
    if elt==num:
        flag=flag+1
        break
    else:
        pass
    count=count+1
if flag==0:
    print("element not found")
else:
    print("element found at ",count)

# not effecient when there is 100 above data