#define
str={} #empty {} is taken as dictionary
print(type(str))
#if u want to create a empty set call set()
str1=set()
print(type(str1))

str1={10,11,12}
print(type(str1))

# inseration order is not preserved
str1={10,11,"hello",12}
print(type(str1))

#update - with the help of another set only
#not possible with index

str1={10,11,"hello",12}
st={60,45}
str1.update(st)
print(str1)

#duplicates not allowed
str1={10,11,"hello",12,11,10}
print(str1)
