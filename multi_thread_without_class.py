##### Multi threading without class #####

from threading import *
import time

##print("current_thread of main is :",threading.current_thread().getName())
##print("current_thread of main is :",threading.current_thread().getName())
##print("current_thread of main is :",threading.current_thread().getName())


##def display():
##    for i in range(10):
##        print("display thread Name is: ",current_thread().getName())
##        time.sleep(1)
##t=Thread(target=display)
##t.start()
##
##
##for i in range(10):
##    print("main program thread name is :",current_thread().getName())
##    time.sleep(1)

def display():
    for i in range(10):
        print("child")
        time.sleep(1)
t=Thread(target=display)
t.start()
for i in range(10):
    print("       Main")
    time.sleep(1)
