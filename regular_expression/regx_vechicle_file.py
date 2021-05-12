from re import *
rule='KL[\d]{2}[a-zA-Z]{2}[\d]{4}'
f=open("vehicles_file","r")
f1=open("vechicles_validated","w")
for line in f:
    vechicle=line.rstrip("\n")
    matcher=fullmatch(rule,vechicle)
    if matcher==None:
        pass
    else:
        f1.write(vechicle)
        f1.write("\n")
f1.close()
