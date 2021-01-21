words="hello hai hello hai hello"
cnt,count=0,0
#print(words.count("hello"))
lst=[]
for word in words:
    w=words.split(" ")
    lst.append(w)
    break
print(lst)
for word in lst:
    for  subword in word:
        if subword =="hello":
            cnt+=1
        elif subword =="hai":
            count+=1
print("count of hello ",cnt)
print("count of hai ",count)
