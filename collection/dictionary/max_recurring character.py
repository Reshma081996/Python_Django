pattern="ABABBACEEEEEEEEEEEEEE"
dict={}
for ch in pattern:#A,B,A
    #print(ch)
    if ch not in dict:#A ,B
        dict[ch]=1#A=1,B=1
    else:#A
        dict[ch]+=1 #A=2
for key,value in dict.items():
    print(key,",",value)
print(dict) #{'A': 3, 'B': 3, 'C': 1, 'E': 14}
#print(dict.get("E")) # VALUE OF E #14
data=sorted(dict,key=dict.get,reverse=True) #['E', 'A', 'B', 'C']
print(data)


