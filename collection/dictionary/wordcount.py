text="hello hai hello hai hello"
words=text.split(" ")
print(words) #['hello', 'hai', 'hello', 'hai', 'hello']
dict={}
for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(dict)

#for key,value in dict.items():
    #print(key,",",value)


#..................................................................................................................
#cnt,count=0,0
#print(words.count("hello"))
#lst=[]
#for word in words:
    #w=words.split(" ")
    #lst.append(w)
    #break
#print(lst)
#for word in lst:
    #for  subword in word:
        #if subword =="hello":
            #cnt+=1
        #elif subword =="hai":
            #count+=1
#print("count of hello ",cnt)
#print("count of hai ",count)
