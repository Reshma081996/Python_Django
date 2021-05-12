#first charc a-k
# second charcter is a num divisible by 3
# folowed by any no of character

from  re import *
vname=input("enter variable name: ")
rule='[a-k][369][a-zA-Z0-9]*'
op=fullmatch(rule,vname)
if op==None:
    print("invalid")
else:
    print("valid")