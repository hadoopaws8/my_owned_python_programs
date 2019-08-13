######## Multi thread without extending class ######

from threading import *
import time

##class student:
##    def display(self):
##        for i in range(10):
##            print("child:",current_thread().getName())
##            time.sleep(1)
##
##s=student()
##t=Thread(target=s.display)
##t1=Thread(target=s.display)
##t2=Thread(target=s.display)
##t.start()
##t1.start()
##t2.start()
##
##for i in range(10):
##    print("Main is : ",current_thread().getName())
##    time.sleep(1)



def doubles(num):
    for i in num:
        time.sleep(0.5)
        print("Doubles: ",2*i)
def squeres(num):
    for i in num:
        time.sleep(0.5)
        print("Squeres: ",i*i)

num=[1,2,3,4,5,6]
begintime=time.time()
#doubles(num)
#squeres(num)
t1=Thread(target=doubles,args=(num,))
t2=Thread(target=squeres,args=(num,))
t1.start()
t2.start()

t1.join()
t2.join()
endtime=time.time()
print("the total time taken :",endtime-begintime)
