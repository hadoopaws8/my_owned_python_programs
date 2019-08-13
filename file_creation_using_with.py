with open(r"C:\Users\jaya\Desktop\calculater\demo1.txt",'w+') as f:
    for i in range(1,31):
        f.writelines("This is "+str(i)+" line\n")
##
##        
##with open(r"C:\Users\jaya\Desktop\calculater\demo1.txt",'r+') as f:
##    data=f.readlines()
##    print(type(data))
##    for i in range(len(data)):
##        if i<10:
##            with open(r"C:\Users\jaya\Desktop\calculater\second.txt",'w') as f1:
##                for j in range(9):
##                    f1.writelines(data[j])
##                    print(j)
##                    print("---------------")
##        elif i>=11 and i<=20:
##            with open(r"C:\Users\jaya\Desktop\calculater\second1.txt",'w') as f1:
##                for j in range(10,20):
##                    f1.writelines(data[j])
##                    print(j)
##        elif i>=21 and i<=30:
##            with open(r"C:\Users\jaya\Desktop\calculater\second2.txt",'w') as f1:
##                for j in range(20,30):
##                    f1.writelines(data[j])
##                    print(j)



##with open(r"C:\Users\jaya\Desktop\calculater\demo1.txt",'w+') as f:
##    for i in range(1,31):
##        f.writelines("This is "+str(i)+" line\n")
##
##        
##with open(r"C:\Users\jaya\Desktop\calculater\demo1.txt",'r+') as f:
##    data=f.readlines()
##    print(type(data))
##    with open(r"C:\Users\jaya\Desktop\calculater\second.txt",'w') as f1: 
##        for j in range(10):
##            f1.writelines(data[j])
##            print(j)
##    with open(r"C:\Users\jaya\Desktop\calculater\second1.txt",'w') as f1:
##        for j in range(10,20):
##            f1.writelines(data[j])
##            print(j)
##    with open(r"C:\Users\jaya\Desktop\calculater\second2.txt",'w') as f1:
##        for j in range(20,30):
##            f1.writelines(data[j])
##            print(j)    

        
with open(r"C:\Users\jaya\Desktop\calculater\demo1.txt",'r+') as f:
    data=f.readlines()
    length=len(data)
    #print(length)
with open(r"C:\Users\jaya\Desktop\calculater\second.txt",'w') as f1: 
    for j in range(10):
        f1.writelines(data[j])
        #print(j)
with open(r"C:\Users\jaya\Desktop\calculater\second1.txt",'w') as f1:
    for j in range(10,20):
        f1.writelines(data[j])
        #print(j)
with open(r"C:\Users\jaya\Desktop\calculater\second2.txt",'w') as f1:
    for j in range(20,length):
        f1.writelines(data[j])
        #print(j)    
