lst1=[1,2,3,4,5]
l=len(lst1)

lst2=[3,4,5,1,2]

def rotate_lst(lst1,lst2):
    shift=int(input("enter how many steps do you want to shift"))
    net_shift=shift%len(lst1)
    #if net_shift==0, for loop imediately ends
    for i in range(net_shift):
        if net_shift>0:
            poped=lst1.pop(len(lst1)-1)
            lst1.insert(0,poped)

        elif net_shift<0:
            poped=lst1.pop(0)
            lst1.append(poped)
    print(lst1)
    #if set(lst2).issubset(lst1):
        #print("list2 is rotation list of list1")
#shift=int(input("enter no of shifts"))

rotate_lst(lst1,lst2)
