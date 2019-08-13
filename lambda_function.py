from functools import reduce
##a=int(input("enter the first element: "))
##b=int(input("enter the first element: "))
##if a>b:
##    print("a is grater then b")
##else:
##    print(b," is grater then ",)

#squire list elements

##l=[2,4,8]
##l1=[]
##for i in l:
##    l1.append(i*2)
##print(l1)

##l1=[]
 ##def squre(l):
##    for i in l:
##        l1.append(i**2)
##   
##sq=squre([2,4,8])
##print(l1)

##l=[2,4,8] 
##sq=lambda a:a*a
##print(list(map(sq,l)))

#addition of two lists
##
##l1=[1,2,3]
##l2=[1,2,3]
##l3=[]
##def add(a,b):
##    for i in range(len(l1)):
##        l3.append(a[i]+b[i])
##add(l1,l2)
##print(l3)

##l1=[1,2,3]
##l2=[1,2,3]
##print(list(map(lambda a,b:a+b,l1,l2)))

#list iterms is grater then 0

##l=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
##l1=[]
##def positive(a):
##    for i in a:
##        if i>0:
##            l1.append(i)
##
##positive(l)
##print(l1)

##print(list(filter(lambda a:a>0, range(-5,6))))


# product of list
l=[1,2,3,4]
##def product(a):
##    
##    for i,j in enumerate(a):
##        c=0
##        print(i,j)
##        c=c+(a[i]+a[i+1])
##        
##    print(c)
##product(l)

product=reduce(lambda x,y:x*y,l)
print(product)
