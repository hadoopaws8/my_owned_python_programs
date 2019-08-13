###hole data read as a string format
##f=open(r"C:\Users\jaya\Desktop\calculater\demo.txt",'r')
##data=f.read()
##print(type(data))
##print(data)

###single line read
##f=open(r"C:\Users\jaya\Desktop\calculater\demo.txt",'r')
####data=f.readline()
####print(type(data))
####print(data)
####print(data)
##print(f.readline())
##print(f.readline())
##print(f.readline())

###multiple lines read
##f=open(r"C:\Users\jaya\Desktop\calculater\demo.txt",'r')
##data=f.readlines()
##print(type(data))
####print(data)
####for i in data:
####    print(i)
##
##############  or  ############
##print(data[0])
##print(data[1])
##print(data[2])

##f=open(r"C:\Users\jaya\Desktop\calculater\demo.txt",'r')
##for x in f:
##    print(type(x))
##    print(x)



f=open(r"C:\Users\jaya\Desktop\calculater\demo.txt",'a')
f.write("\nhi jayaram\n")  #same line you have to enter you need to insert for newline is \n
f.close()
f=open(r"C:\Users\jaya\Desktop\calculater\demo.txt",'r')
print(f.read())
f.seek(0)        #seek select offset value 
print(f.read())



### Program to show various ways to read and 
### write data in a file. 
##file1 = open(r"C:\Users\jaya\Desktop\calculater\myfile.txt","w") 
##L = ["This is Delhi \n","This is Paris \n","This is London \n"]  
##  
### \n is placed to indicate EOL (End of Line) 
##file1.write("Hello \n") 
##file1.writelines(L) 
##file1.close() #to change file access modes 
##  
##file1 = open(r"C:\Users\jaya\Desktop\calculater\myfile.txt","r+")  
##  
##print ("Output of Read function is ")
##print (file1.read())
##print
##  
### seek(n) takes the file handle to the nth 
### bite from the beginning. 
##file1.seek(2)  
##  
##print ("Output of Readline function is ")
##print (file1.readline()) 
##print
##  
##file1.seek(0) 
##  
### To show difference between read and readline 
##print ("Output of Read(9) function is ")
##print (file1.read(9)) 
##print
##  
##file1.seek(0) 
##  
##print ("Output of Readline(9) function is ")
##print (file1.readline(9)) 
##  
##file1.seek(0) 
### readlines function 
##print ("Output of Readlines function is ")
##print (file1.readlines()) 
##print
##file1.close() 
##
##
##
