import csv
import random
import time
import os.path
from os import path

def load_data(file_path):
    fields=["name","stock"]
    if path.exists(file_path):
        l=[]
        count=0
        print("name"," ","stock")
##        while True:
##            time.sleep(1)
        with open(file_path,'w',newline="") as f:
            writer=csv.DictWriter(f,fieldnames=fields)
            writer.writeheader()
            while True:
                time.sleep(1)
                rand=random.randrange(1000,9999)
                writer.writerow({"name":"jayaram","stock":rand})

                l.append(["jayaram",rand])
                print(l[count][0],l[count][1])
                count+=1

##            with open (file_path) as j:
##                reader = csv.reader(j)
##                for i in reader:
##                    print(i[0],i[1])
    else:
        with open(file_path,'w',newline="") as f:
            writer=csv.DictWriter(f,fieldnames=fields)
            writer.writeheader()
            #writer.writerow({"name":"jayaram","stock":random.randrange(1000,9999)})
    
load_data(r'C:\Users\jaya\Desktop\data1.csv')
