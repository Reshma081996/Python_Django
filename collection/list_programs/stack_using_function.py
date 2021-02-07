
size=int(input("enter size: ")) #2
stk=[]
top=0
ch=1
#choice=int(input("enter choice - 1.Push\t 2.Pop\t3.Display:  "))
def push():
    global top #0
    if top>=size: #0>=2
        print("stack overflow i.e full ")

    else:
        elt=int(input("enter element")) #1 --after push
        stk.insert(top,elt)#(0,1)
        #print(top)
        top+=1#1

def pop_items():
    global top#1
    if top<=0:#0
        print("stack underflow  i.e empty ")
    elif top>0:#1>0
        top-=1#1-1=0
        #stk.pop()
        print(stk[top],"is poped out")#stk[0]
        #print(top)#0

def display():
    for i in range(0,top):
        print(stk[i])

while(ch!=0):

    choice=int(input("enter choice - 1.Push\t 2.Pop\t3.Display:  "))
    if choice==1:
        push()

    elif choice==2:
        pop_items()

    elif choice==3:
        display()
    ch = int(input("enter do u want to continue"))
