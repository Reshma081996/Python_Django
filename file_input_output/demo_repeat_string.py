f=open("demo","r")
#lst=[]
#lst1=[]
dict={}
for line in f:
    #print(line)
    word=line.rstrip("\n").split(" ")
    print(word)
    #lst.append(word)
#print(lst) #[['this', 'is'], ['a', 'demo'], ['text', 'file'], ['test', 'test']]

#for words in lst:#outer loop

    for subword in word:#inner loop
        #lst1.append(subword) #flattening of list
        #['this', 'is', 'a', 'demo', 'text', 'file', 'test', 'test']

        if subword not in dict:
            dict[subword]=1
        else:
            dict[subword]+=1
            
#print(lst1)
print(dict)
for k,v in dict.items():
     print(k,"==========>",v)
data=sorted(dict,key=dict.get,reverse=True)
print("maximum repeating word : ",data[0])



