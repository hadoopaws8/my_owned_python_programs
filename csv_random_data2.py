import csv
import random
import time


def load_data(file_path):
    fields=["Id","Stock1","Stock2"]
    l=[]
    count=0
##    print("Id","Stock1","Stock2")
    try:
        with open(file_path,'w',newline="") as f:
            print("\t","Id","Stock1","Stock2")
            print("\t------------------")
            writer=csv.DictWriter(f,fieldnames=fields)
            writer.writeheader()
            try:
                while True:
                    time.sleep(1)
                    rand=random.randrange(1000,9999)
                    rand1=random.randrange(1000,9999)
                    writer.writerow({"Id":count+1,"Stock1":rand,"Stock2":rand1})

                    l.append([count+1,rand,rand1])
                    print("\t",l[count][0]," ",l[count][1]," ",l[count][2])
                    count+=1
            except KeyboardInterrupt as e:
                print("\t------------------")
                print("\tyour program is END")
            except Exception:
                print("unknown exception")
    except PermissionError:
        print()
        print("\t\t\t-------------------------")
        print("\t\t\tplease close the CSV file")
        print("\t\t\t-------------------------")
    except Exception as e:
        print(e)
        
load_data(r'C:\Users\jaya\Desktop\data1.csv')
