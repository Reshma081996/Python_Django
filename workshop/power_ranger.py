n=int(input("enter num")) #2
#r=int(input("enter upto which num power is to be calculated"))
low=int(input("enter low limit")) #48
high=int(input("enter high limit"))#65
for i in range(1,high):# 1 in (1, 100)
    res= i**n # 1**2
     #print(res)
    if (res>=low) and (res<=high):# 1>=48 and 2<=65
        print(res)