from re import *
rule='[a-zA-Z0-9.]*@[a-z]*.com'
f=open("mail_details","r")
f1=open("mail_valid","w")
for line in f:
    mail_mail=line.rstrip('\n')
    #print(mail_mail)
    matcher=fullmatch(rule,mail_mail)
    if matcher==None:
        pass
        #print("ivalid")
    else:
        f1.write(mail_mail)
        f1.write("\n")
f1.close()

