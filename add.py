n=input("enter the calculation: ")
n.split()
l=[]
for i in n:
    l.append(i)
#print(l)
a=int(l[0])
b=int(l[2])
#print(str(l[1]))
if str(l[1])=="+":
    print(a,"+",b,"=",a+b)
elif str(l[1])=="-":
    print(a,"-",b,"=",a-b)
elif str(l[1])=="*":
    print(a,"*",b,"=",a*b)
elif str(l[1])=="/":
    if b>0:
        print(a,"/",b,"=",a/b)
    else:
        print(a,"is not divisiable by",b)
else:
    print("invalid operation")
