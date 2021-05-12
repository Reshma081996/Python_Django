
#exception-
#try, except,finally


#file not found
#index out of bound
#zero division error
#type error


num1=int(input("enter num1"))
num2=int(input("enter num2"))
#res=num1/num2 #doubtful code
#print(res) #ZeroDivisionError: division by zero
try:#doubtful code
    res=num1/num2
    print(res)
except Exception as e:#exception handling
    print("zero division error ocuured")
finally:#mandatory code
    print("databse connection")

