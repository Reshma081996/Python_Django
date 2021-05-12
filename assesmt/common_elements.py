
lst1=[10,2,3,4,5,6,7,13]
lst2=[12,16,3,5,7,9,10,11]
a=sorted(lst1)#[2, 3, 4, 5, 6, 7, 10, 13]
print(a)
b=sorted(lst2)#[3, 5, 7, 9, 10, 11, 12, 16]
print(b)
low_a=0
high_a=len(lst1)-1
low_b=0
high_b=len(lst2)-1

while(low_a<high_a and low_b<high_b):

    if lst1[low_a] in lst2[low_b]:
        print(low_a)

    else:

        low_b+=1
        low_a+=1

