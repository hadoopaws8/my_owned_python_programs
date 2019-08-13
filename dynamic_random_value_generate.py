import csv
##import random
##import time
##count=1
##try:
##    
##    while True:
##        time.sleep(0.5)
##        print(count," ",random.randrange(1000,10000)," ",random.randrange(1000,10000) )
##        with open(r"C:\Users\jaya\Desktop\randomoutput.csv",'a+') as f:
##            write=csv.writer(f,delimiter=',')
##            write.writerows(count,random.randrange(1000,10000),random.randrange(1000,10000))
##        count+=1
##except KeyboardInterrupt as e:
##    print("your program is end")
##except Exception as e:
##    print("This is unknow exception")
##



##with open(r"C:\Users\jaya\Desktop\calculater\randomvalue.txt",'w+') as f:
##    for i in range(10):
##        f.writelines(str(random.randrange(100,1000))+"\n")


##row = [3,"jayaram","polakala"]
##with open(r'C:\Users\jaya\Desktop\people1.csv', 'a') as csvFile:
##    writer = csv.writer(csvFile)
##    writer.writerow(row)
##csvFile.close()

person = [['SN', 'Person', 'DOB'],
['1', 'John', '18/1/1997'],
['2', 'Marie','19/2/1998'],
['3', 'Simon','20/3/1999'],
['4', 'Erik', '21/4/2000'],
['5', 'Ana', '22/5/2001']]
csv.register_dialect('myDialect',
quoting=csv.QUOTE_ALL,
skipinitialspace=True)
with open(r'C:\Users\jaya\Desktop\people1.csv', 'w') as f:
    writer = csv.writer(f, dialect='myDialect')
    for row in person:
        writer.writerow(row)
f.close()
