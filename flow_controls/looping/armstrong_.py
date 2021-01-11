#1**3+5**3+3**3 ie 153 is armstrong num
num=int(input("enter num"))#153
res=0
while(num>0):#153>0, 15>0
    digit=num%10# 153%10=3, 15%10=5 ,1%10=1
    #print(digit)#3,5,1
    res=res+digit**3 #0+3**3,27+5**3,152+1**3
    num = num // 10  # 5,1,0
print(res)#27,152,153



