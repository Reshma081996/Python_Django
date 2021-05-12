lst=[10,20,30]
squares=[num**2 for num in lst]
print(squares)

lst1=[[10,20],[30,40],[50,60]]
ans=[num for ls in lst1 for num in ls]
print(ans)


#find even num  from given list using list comphrension
lst2=[1,2,3,4,5,6,7,8,9,10]
#l=len(lst2)+1
#for num in range(1,l):
    #print(num)
    #if num%2==0:
        #print(num)
even=[num for num in range(1,len(lst2)+1)  if num%2==0]
print(even)
odd=[num for num in range(1,len(lst2)+1) if num%2!=0]
print(odd)