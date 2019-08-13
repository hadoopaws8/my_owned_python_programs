import random
import time
l=[]
count=0
while True:
    l.append(random.randrange(1000,9999))
    time.sleep(1)
    print(l[count])
    count+=1
