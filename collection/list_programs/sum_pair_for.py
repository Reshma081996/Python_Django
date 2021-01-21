#[1,2,3,4] imp=6 (4,2) op=(3,4)

lst=[1,2,3,5]

# i  0 1 2 3
#j     * ?        j=i+1
value=int(input("enter num"))#6
for i in range (0,len(lst)):#0,1
    for j in range(i+1,len(lst)):#1 in (1,4),2,3,not4; [2,3 in(2,4)]
        if (lst[i]+lst[j]==value):#lst[0]+lst[1]=1+2=3;lst[0]+lst[2]=1+3=4;lst[0]+lst[3]=1+4=5
            #lst[1]+lst[2]=2+3=5; lst[1]+lst[3]=2+4=6
            print("pairs are:",(lst[i],lst[j]))
            break
        else:
            pass














#low=0
#upp=len(lst)-1
#while(low<upp):#1<4
    #res=lst[low] + lst[upp] #1+4=5
    #if res==value:
        #print("pairs : ",(lst[low] ,lst[upp]))
        #break
    #else:
        #low += 1