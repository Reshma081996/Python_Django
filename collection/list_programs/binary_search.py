#[5,6,7,8,10,11,12]
# 0               6
#l      m         upp
#sort
#set lw, high
#while (lw<high)
#calculate mid
#if elt<lst[mid] , up=mid-1
#if elt>lst[mid], low=mid+1
#if elt==lst[mid]

# binary search applicable to only numbers
lst=[10,8,7,11,12,6,5]
lst.sort()
print(lst)
low=0
high=len(lst)-1

elt=int(input("enter element to be searched"))
flg=0
while(low<=high):#0<=6, 4<=6, 6<=6
    mid = (low + high) // 2 #0+6//2=3 ; 4+6//2=10//2=5
    if elt<lst[mid]: #12 < lst[3] , 12<8 ; 12<lst[5], 12<11 ,12<6
        high=mid-1

    elif elt>lst[mid]:# 12>LST[3]=12>8; 12>11
        low=mid+1 # low=mid+1=3+1=4 , low=mid+1=5+1=6

    elif elt==lst[mid]:#12==lst[6]
        flg=flg+1 #flag=1
        break

if flg==0:
    print("element not found")
else:
    print("element found")
#12 elt found