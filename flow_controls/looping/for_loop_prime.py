#check num is prime or not : num divisible by 1 and itself is prime

num=int(input("enter num"))#11,8,9
flag=0 #prime num
if (num==1):#11!=1, 8!=1 ,9!=1
    print("not prime")
else:#11,8 ,9
    for i in range(2,num): #11,8 ,9
        if(num%i==0):#11%2!=0,8%2==0 ,9%2!=0,9%3==0
            flag = 1
            i+=i #3
            break

        else:
            flag=0
    if(flag==0):
        print(num," is prime ")
    else:
        print(num," is not prime")
