from re import *
rule='\d{10}'
f=open("phoneno_details","r" )
f1=open("phone.txt","w")
for line in f:
    phone=line.rstrip("\n")
    print(phone)
    matcher=fullmatch(rule,phone)
    #print(matcher)
    if matcher==None:
        pass
    else:

        f1.write(phone)
        f1.write("\n")

f1.close()
