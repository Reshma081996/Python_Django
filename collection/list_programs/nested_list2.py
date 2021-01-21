lst=[[10,20],[21,22],[51,52],[53,54,55,56]]
#op=[10,20,21,22,51,52,53,54]
#flattened

lst1=list()
for sublist in lst: #[10,20]
    for number in sublist:#10
        lst1.append(number)
print(lst1)

