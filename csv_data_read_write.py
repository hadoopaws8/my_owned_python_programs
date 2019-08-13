import csv
import time
##with open(r"C:\Users\jaya\Desktop\data.csv","w+") as csvfile:
##    writer=csv.writer(csvfile)
##    writer.writerow(["col 1","col 2"])
##    writer.writerow(["data 1","data 2"])
##
##with open(r"C:\Users\jaya\Desktop\data.csv","r") as csvfile:
##    reader=csv.reader(csvfile)
##    
##    for row in reader:
##        print(row)
##        #print(type(row))

##with open(r"C:\Users\jaya\Desktop\data.csv","a") as csvfile:
##    writer=csv.writer(csvfile)
##    writer.writerow(["Data 3","Data 4"])


##with open(r"C:\Users\jaya\Desktop\data.csv","r") as csvfile:
##    reader=csv.DictReader(csvfile)
##    for row in reader:
##        print(row)
##        print(type(row))

##with open(r"C:\Users\jaya\Desktop\data.csv","w") as csvfile:
##    fieldnames = ["id","title"]
##    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
##    writer.writeheader()
##    writer.writerow({"id":123,"title":"New title"})
##    writer.writerow({"id":152,"title":"Jayaram"})
##



def get_length(file_path):
    with open(r"C:\Users\jaya\Desktop\data.csv")as csvfile:
        reader=csv.reader(csvfile)
        reader_list=list(reader)
        print(reader_list)
        return len(reader_list)
##    return 1
def append_data(file_path,name,email):
    fieldnames=["id","name","email"]
    #the number of rows?
    next_id = get_length(file_path)
    with open(file_path,"a",newline='') as csvfile:
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({
            "id":next_id,
            "name":name,
            "email":email,
            })
append_data(r"C:\Users\jaya\Desktop\data.csv","justin","hello@teamcfe.com")
