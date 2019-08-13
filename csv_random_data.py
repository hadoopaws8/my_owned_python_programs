import csv
import random
import time
import os.path
from os import path

def load_data(file_path):
    fields=["name","stock"]
    if path.exists(file_path):
        with open(file_path,'a',newline="") as f:
            writer=csv.DictWriter(f,fieldnames=fields)
            #writer.writeheader()
            writer.writerow({"name":"jayaram","stock":random.randrange(1000,9999)})
    else:
        with open(file_path,'w',newline="") as f:
            writer=csv.DictWriter(f,fieldnames=fields)
            writer.writeheader()

        
#load_data(r'C:\Users\jaya\Desktop\data1.csv')
def display(file_path):

    with open(file_path,'r') as f:
        reader=csv.reader(f)
        for i in reader:
            print(i[0],i[1])
            #print(type(i))
while True:
    time.sleep(0.5)
    load_data(r'C:\Users\jaya\Desktop\data1.csv')            
    display(r'C:\Users\jaya\Desktop\data1.csv')

    
