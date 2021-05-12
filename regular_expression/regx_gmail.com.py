#gmail.com
from re import *

mail=input("enter ur gmail: ")
rule='[a-zA-Z0-9.]*@gmail.com'
matcher=fullmatch(rule,mail)
if matcher==None:
    print("invalid mail")
else:
    print("valid mail")