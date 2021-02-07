#def add(num1,num2):
    #return num+num2

#lambda functions - reduce length of code, concise code
add=lambda num1,num2:num1+num2
print(add(10,20))

cube=lambda x:x**3
print(cube(2))

even=lambda num:num%2==0
print(even(20))

#map:no of input equal to o/p
lst=[1,2,3,4,5,6]
#filter: only even nos. no of input not equal to o/p
#reduce:sum(list),highest value,min value,1 o/p

lst=[1,2,3,4,5,6]
#create a list and use map with 2 arguements ,
#           sqlist=map(func,iterables)
#def sq:
   # return num**2

sqlst=list(map(lambda num:num**2,lst))
print(sqlst)

lst=[1,2,3,4,5,6]
sqlst1=list(map(lambda num:num-1 if num<5 else num+1 if num>5 else num,lst)) #cant give elif directly
print(sqlst1)

evens=list(filter(lambda num:num%2==0,lst))
print(evens)

odd=list(filter(lambda num:num%2!=0,lst))
print(odd)

names=["india","pak","aus","eng","sa","sreelinka","aukland","indonesia"]
namelst=list(map(lambda name: name.upper(),names))
print(namelst)

#starting with a
acountry=list(filter(lambda name:name[0]=='a',names))
print(acountry)

# cant use reduce directly import from functools
from functools import reduce
lst=[10,11,12,13,14]
sum=reduce(lambda no1,no2:no1+no2,lst)
print(sum)

high=max(reduce(lambda no1,no2:no1 if no1>no2 else no2,lst ))
print(high)

mini=min(reduce(lambda no1,no2:no1 if no1<no2 else no2,lst ))
print(mini)
