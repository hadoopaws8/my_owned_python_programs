from threading import *
import time

class Hello(Thread):
    def run(self):           # here run function must and should for call stat method
        for i in range(5):
            print("HELLO",end=" ")
            time.sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("HI")
            time.sleep(1)

t1=Hello()
t2=Hi()


t1.start()
time.sleep(0.5)
t2.start()

t1.join()
t2.join()

print("bye")

