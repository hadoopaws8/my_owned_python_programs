##### Multi threading using extending class #########

from threading import *
import time

class student(Thread):
    def run(self):
        for i in range(10):
            print("child :",current_thread().getName())
            time.sleep(1)
s=student()
s1=student()

s.start()
s1.start()

for i in range(10):
    print("main display:",current_thread().getName())
    time.sleep(1)
s.join()
s1.join()
print("*******bye bye bye*******")
