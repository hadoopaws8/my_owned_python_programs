import random
import os

##l=[]
##for i in range(10):
##    l.append(random.randrange(100,1000))
##print(l)
##if os.path.exists(r"C:\Users\jaya\Desktop\calculater\randomvalue.txt"):
##    os.remove(r"C:\Users\jaya\Desktop\calculater\randomvalue.txt")
##else:
##    print("you don't hove the file")
with open(r"C:\Users\jaya\Desktop\calculater\randomvalue.txt",'w+') as f:
    for i in range(10):
        f.writelines(str(random.randrange(100,1000))+"\n")
with open(r"C:\Users\jaya\Desktop\calculater\randomvalue.txt",'r+') as f:
    data=f.readlines()
    for i in data:
        print(i)
    print("The 7th index of the element is : ",data[6])
    print("The 8th index of the element is : ",data[7])
    
