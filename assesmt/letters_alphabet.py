#number=[]
def GroupTotals(strArr):
    number=[]
    for letters in strArr:
        print(letters)
        numbers=ord(letters) - 96
        number.append(numbers)
    return number

strArr=input("Enter String : ")
data=GroupTotals(strArr)
print(data)
