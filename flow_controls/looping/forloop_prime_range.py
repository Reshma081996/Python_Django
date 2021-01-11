low=int(input("enter lower limit"))#2
upp=int(input("enter upper limit")) #12

for num in range(low,upp):# (2,12),(3,12).................(11,12)
    flg = 0
    for i in range(2,num):#2 in range(2,2)
        if (num%i==0):#2%2!=0,5%2!=0,,6%2==0
            flg=flg+1
            #print("non-prime num are ")
            #print(num)
            break
        else:
            flg=0
    if flg==0:
        print("prime nums")
        print(num)


