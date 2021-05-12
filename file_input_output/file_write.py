f=open("write.txt","w") # write - rewrite file ,same for apend
names=["abh","lmn","fff"]
for name in names:
    f.write(name+"\n")
f.close()