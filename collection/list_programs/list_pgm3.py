lst=[10,11,12,13,14,15,16,17]
even=list()
odd=list()
for num in lst:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(even)
print(odd)
print("sum of even list",sum(even))
print("sum of even list",sum(odd))

