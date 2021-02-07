# read movie file
f=open("movies.csv","r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(",")
    #print(words)
    year=words[2]
    if year not in dict:
        dict[year]=1
    else:
        dict[year]+=1

for k,v in dict.items():
    print(k,"===========>",v)

data=sorted(dict,key=dict.get,reverse=True)
print(data[0],"with",dict.get(data[0]),"movies")

