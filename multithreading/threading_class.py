from threading import *

class Mythread(Thread):
    def run(self):
        for i in range(1,10):
            print("child thread inside")

obj=Mythread()
obj.start()

for i in range(1,10):
    print('main thread excuton')