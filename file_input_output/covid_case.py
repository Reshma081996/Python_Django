f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(",")
    state=words[3].rstrip"***")
    #print(state)
    if state=="Telengana":
        state="Telangana"
    confirmed_cases=int(words[8])
    
    if state not in dict:
        dict[state]=confirmed_cases

    else:
        dict[state]=confirmed_cases

#print(dict)
for k ,v in dict.items():
    print(k,"======>",v)
res=sorted(dict,key=dict.get,reverse=True) #HIgh to low that is maharastra
print(res)
print(res[0],dict.get(res[0]))#Maharashtra 1859367

#alpabatic order of state name
result=sorted(dict)
print(result)


