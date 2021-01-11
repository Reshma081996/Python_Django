# read num, low,upp and find num**2 and checkn num in btwn low and upp
num=int(input("enter num")) #2
low=int(input("enter lower limit")) #3
upp=int(input("enter upper limit")) #10

for i in range(1,upp+1):#for 1 in range (1,11),2 in (1,11)
    res=i**num #res=1**2=1,2**2=4
    if (res>=low) and (res<=upp):#1!>=3 and 1!<=11,4>=3 and 4<=11
        print(i)#2
