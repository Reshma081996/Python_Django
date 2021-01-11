lower_=int(input("enter limit"))#2
up=int(input("enter upper"))#8

while(lower_<=up):#2<=8,3<=8,4<=8
    if(lower_%2==0):#2%2=0,#3%2!=0,4%2==0
        print("even num:",lower_)#2,4
    lower_+=1#3,4

