##l=[1,1,1,2,2,3]
##
##ln=len(l)
##s=set(l)
##li=list(s)
##for i in li:
##    count=0
##    for j in l:
##        if i==j:
##            count+=1
##            if count>=ln/2:
##                k=count
##    print(i,"=", count)
###print(k)
##try:
##    if k<=ln/2:
##        print("High frequency of element is : ")
##except Exception as e:
##    
##    pass



##l=[5,1,2,5,5,3,5,2,3,5]
##
##ln=len(l)
##s=set(l)
##li=list(s)
##k=0
##d={}
##for i in li:
##    count=0
##    for j in l:
##        if i==j:
##            count+=1
##            if count>k:
##                k=count
##    d[i]=count
##    #print(i,"=", count)
###print(d)
###print(k)
##for i in d:
##    if d[i]==k:
##        print("Hi feqency element in list is :",i)
##        if k>=ln/2:
##            print("This feqency is heigher then half of the list")



from collections import Counter

l=[5,5,2,5,5,3,5,2,3,5]
#l=[2,2,2,2,2,3,3,3,3,3]
ln=len(l)
k=Counter(l)
#print(k)
for key,value in k.items():
    #print(key,"-->",value)
    if value >ln/2:
        print(key,"-->",value)
        k=value
try:
    if k>=ln/2:
        print("The list has contained one element more freqency")
except Exception:
    print("less freqency")


