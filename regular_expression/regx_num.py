
#vahicle num #KL2DIGIT2ALPAHAETS4DIGIT


from re import *
reg_no=input("enter registration no: ")
rule='KL[0-9]{2}[a-zA-Z]{2}[0-9]{4}'
#rule='(91)?\d{10}'

#rule='[a-zA-Z.]*[\d]*gmail.com'
match=fullmatch(rule,reg_no)#
if match==None:
    print("inavlid  reg num")
else:

    print("valid reg num")


    #phone num validation from file
    #mail id
    #vechile reg