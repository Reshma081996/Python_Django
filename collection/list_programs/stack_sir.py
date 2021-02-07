size = int(input("enter size: "))  # 2,-1,0
stk = []
top = 0
ch=1
def push():
    global top
    if top>=size:
        print("stack is full")
    else:
        elt=int(input("enter element"))
        stk.insert(top, elt)
        top+=1

def pop_items():
    global top

    if top<=0:
        print("empty stack")
    elif top>0:
        top-=1
        print(stk[top], " is poped out")


def display():
    #print(stk)
    for i in range(0,top):
        print(stk[i])

    #print(stk)

while (ch != 0):
    choice = int(input("enter choice - 1.Push\t 2.Pop\t3.Display:  "))
    if choice == 1:
        push()

    elif choice == 2:
        pop_items()

    elif choice == 3:
        display()
    ch = int(input("enter do u want to continue"))
