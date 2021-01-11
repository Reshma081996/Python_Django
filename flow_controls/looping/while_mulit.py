#print multiplication table in the format 2*1=2

num=int(input("enter num whose multiplication table is required"))
num2=int(input("enter num upto which multiplication table is required"))
i=1
while(num>=0):#2>=0,2>=0,2>=0
    if(i<=num2):#1<=12,2<=12,3<=12,4<=12
        mult=i*num #1*2=2,2*2=4,3*12,
        print(i,"*",num,"=",mult)
    i+=1  #2,3,4






