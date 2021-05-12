import threading
import time

def display():
    for i in range(1,10):
        time.sleep(5)
        print("executing child thread")
    print(threading.currentThread().getName())


t=threading.Thread(target=display)# creating new thread OBJ
t.start()
t.join() # t complete ayit excute chaiytha shesham mathram main thread excute chaiyan paadullu
begintime=time.time()

#print("begintime:",begintime)

for i in range(1,10):
    time.sleep(5)
    print("exceuting main thread")
print(threading.currentThread().getName())
endtime=time.time()
#print("endtime:",endtime)
totaltime=endtime-begintime
print("total time taken:",totaltime)


"""
mrg
        t1          t2              t3=t1.join() t2.join()
        p1          p2              p3
        datefix ,bookauditoruim invite
"""