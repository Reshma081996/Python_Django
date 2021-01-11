# 123 to 321 - reverse
num=int(input("enter num")) #123
res=""
while(num>0):#123>0
    digit=num%10
    res=res+str(digit)
    num=num//10
print(res)
if((int(res))==num):
    print("plaindrome")