pattern="ABABBAC"
dict={} # use hashing technique
#Find first recursive character - first adyam repeat chaiyuna character
for ch in pattern: #print each character one by one
    print(ch)
    if ch not in dict:
        dict[ch]=1
    else:
        print(ch,"is recursive character")
        break
