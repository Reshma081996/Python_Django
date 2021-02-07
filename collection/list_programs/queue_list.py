
#queue is a ds containing list of elements  in which insertion and deletion ocuur at 2 ends
#insertion at rear -enqueue , last item present in rear
#deletion at front -dqueue , first entered elmt deltd first

queue=[]
size=int(input("Enter Size : "))
#rear=0 #2
#front=0
ch=1
def insertion():
    #global  rear,front #1,2
    if len(queue)==size:
    #if rear>=size:#0>=2,1>=2,2>=2
        print("Queue overflow ie full")# full
    else:
        element=int(input("Enter element")) #11,12
        queue.append(element)
        #queue.insert(0,element) #(0,11)(1,12)
        #rear+=1 #0+1,1+1
        #front=0


def deletion():
    #global front,rear #f=0,r=2,f=1

    #print("f=",front)
    if len(queue)==0:
        print("Empty Queue")

    else:
        print(queue.pop(0),"popped out")
        #print(queue[0],"popped out ")#0--> 11,1--->12
        #front += 1

        #front+=1 #0+1,1+1=2
        #print(front)



def display():
    pass
    #global front,rear
    for i in range(0,len(queue)):
       print(queue[i])


while(ch!=0):
    choice=int(input("enter choice 1.Insertion\t 2.Deletion \t3.Display"))
    if choice==1:
        insertion()
    elif choice==2:
        deletion()
    elif choice==3:
        display()
    ch=int(input("Do you want to continue?,Press 1"))