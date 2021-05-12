lst=[10,12,13]
position=int(input("enter position"))
num1=int(input("enter num1"))
num2=int(input("enter num2"))

#print(lst[position])#ist index out of range
try:
    res=num1/num2 #exception occured,code terminated
    print(lst[position])
except Exception as e:
    print(e.args)
    #print("index out of bound")#exception handling

