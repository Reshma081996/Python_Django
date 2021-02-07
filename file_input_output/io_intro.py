#read
#write
#append

#step1: we have to create reference
#f=open("filepath","mode")

#for lines in f:
    #print(lines)
    #break #fiRST line mathram

f=open("demo","r")
word=list()
lst=list()
for lines in f:
    wrd=lines.rstrip("\n").split(" ")
    word.append(wrd)
    #for words in lines:
        #st.append(words)
print(word)
for  line in word:
    for subword in line:
        lst.append(subword)

print(lst)


