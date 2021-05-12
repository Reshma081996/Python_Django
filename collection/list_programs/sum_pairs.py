lst=[1,2,3,5]
lst.sort()
low=0
upp=len(lst)-1
num=int(input("enter element"))# 3 ; 6 ;7

while(low<=upp):# 0<=3,0<=2,0<=1; 0<=3 ; 0<=3 ; 1<=3
    total=lst[low]+lst[upp]# lst[0]+lst[3]=1+5=6,lst[0]+lst[2]=1+3=4,lst[0]+lst[1]=1+2=3
    #lst[0]+lst[3]=1+5=6 ; lst[0]+lst[3]=1+5=6 , lst[1]+lst[3]=2+5
    if num==total:# 3!=6, 3!=4, 3=3 ;6==6 ; 7!=6 ,7==7
        print("pairs are ",(lst[low],lst[upp])) #(1,2) ;(1,5); (2,5)
        upp-=1
        low+=1

    elif num<total: #3<6 ; 7<6
        upp-=1 #value=3,2
    elif num>total: #6
        low+=1 # 0+1=1
