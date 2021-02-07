#-------------------------------------------------------------------------------------------------------------------
# data structures  - logical represenation of data in computers memory; way of storing , organising and retrieving
#data in an effecient way for optimal performance,
#LIST-sequential ds ,dynamic, hetergenous elemts, through list implement concepts like stack and q
#***************************************************************************************************************
#           types of ds

#linear ds -store data in consecutive memory location-
# 1.STACK(REVERSE STRING,POLISH STRINGS)
# 2.QUEUE(customer service at call centre)
#3.array

#non-linear-tree,linked list,graph,binary search tree
#linked list
#node[data, next]---->[data, next]---->[data, next]
#.........a.............b..............c
#a[next] stores address of b

#stack is linear ds and inseration & remve data occur at one end called top of stack
# 2 operations -push and pull
#lifo last in first out
#------------------------------------------------------------------------------------------------------------

stk=[]#3,4
size=int(input("enter size of stack")) #2
top=0
ch=1
#choice = int(input("enter ur choice:\n1.push\n2.pop\n3.display\n"))
while (ch!=0):
    choice = int(input("enter ur choice:\n1.push\n2.pop\n3.display\n"))#1,1
    if choice==1:#1
        if top>=size:#0>=2,1>=2,2>=2
            print("stack overflow")

        elif top<size:#0<2,1<2,2<2
            element = int(input("enter element:"))#3,4
            stk.append(element)#3,4
            top+=1 #1,2

    elif choice==2:

        if top<=0:#
            print("stack underflow -empty")
        else:
            top -= 1
            stk.pop()


    elif choice==3:

      for i in range(0,top):
          print(stk)
    ch=int(input("enter do u want to continue"))



