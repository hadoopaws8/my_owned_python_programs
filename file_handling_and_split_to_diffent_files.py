#import operator
##lines_seen =set()
##outfile = open(r"C:\Users\jaya\Desktop\calculater\demo21.txt",'w')
##for line in open(r"C:\Users\jaya\Desktop\calculater\demo2.txt",'r'):
##    if line not in lines_seen:
##        outfile.write(line)
##        lines_seen.add(line)
##print(lines_seen)
##outfile.close()


with open(r"C:\Users\jaya\Desktop\calculater\demo2.txt",'r') as f, open(r"C:\Users\jaya\Desktop\calculater\demo21.txt",'w') as f1:
    data=f.readlines()
    lines_seen=set()
    for i in data:
        if i not in lines_seen:
            f1.write(i)
            lines_seen.add(i)
            
with open(r"C:\Users\jaya\Desktop\calculater\demo2.txt",'r') as f, open(r"C:\Users\jaya\Desktop\calculater\demo22.txt",'w') as f2:
    data=f.readlines()
    next_seen=set(data)
    for i in next_seen:
        if (i in data)and data.count(i)!=1:
            f2.write(i)
            
with open(r"C:\Users\jaya\Desktop\calculater\demo2.txt",'r') as f, open(r"C:\Users\jaya\Desktop\calculater\demo23.txt",'w') as f3:
    data=f.readlines()
    data1=data
    data2=[]                # this is for value checking
    data3=[]
    for i in data1:
        data2.append(i.split("#")[2])
        #print(i.split("#"))
    #print(data2)
    
    s=set(data2)           # this for duplicates remove if not remove the for is repeat multiple times 
    data2=list(s)
    #print(s)
    data2.sort()           # it is for shorting the values 
    #print(data2)
    for i in range(len(data2)):         #here only 4 values will check
        for j in data:
            if data2[i]==j.split("#")[2]:    #each and every time check with i value is equel and append the list
                data3.append(j)
                f3.write(j)
    print(data3)
    

        
        
