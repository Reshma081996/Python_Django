from threading import  *
import  time

class  Mythread:
    def job(self):
        for i in range(10):
            time.sleep(2)
            print("child thread")
obj=Mythread()
t=Thread(target=obj.job)
t.start()


    time.sleep(2)
    print("main thread ")