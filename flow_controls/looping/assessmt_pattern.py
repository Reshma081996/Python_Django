#2+22
#3+33+333
#4+44+444+4444
num=int(input("enter num")) #"2"
i=1
data=0
while(i<=num):#1<=2,2<=2
    res=(str(num))*i #"2"*1="2","2"*2="22"
    print(res)    #"2","22"


    data+=int(res)
    i+=1#2,3
print(data)#2,24