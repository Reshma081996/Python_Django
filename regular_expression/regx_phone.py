
#10 digits
from re import *
ph_no=input("enter phone num: ")
rule='(91)?[0-9]{10}'
matcher=fullmatch(rule,ph_no)
if matcher==None:
    print('invalid phone number')
else:

    print('valid phone number')
