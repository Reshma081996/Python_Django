n=int(input("enter num"))#2
if 1<=n<=9 : # 1<2<=9
    digit = 0
    for i in range (1,n+1):#(1 in (1,2):,2 in (1,3)
        result=(str(n))*i # res=2*1="2",2*2="22"
        print(result)#2, 22
        digit+=int(result)#0+int(2)=2, 2+int(22)
    print("sum of series = ",digit)# 24








    #2+22
    #3+33+333
