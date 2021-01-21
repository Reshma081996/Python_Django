str1=input("enter a string")
l1=input("enter one letter")
l2=input("enter second letter")
length=len(str1)
flg=0
if not str1.islower():
    print("enter string in lower case")
else:
    for i in range(length):
        if str1[i]==l1:
            index=i
    for i in range(length):
        if str1[i] == l2 and i<index:
            flg=1

    if flg==0:
        print("true")
        print(l1+" occur before "+l2)
    else:
        print("false")

