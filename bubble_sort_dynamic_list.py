import random
def bubble_sort(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j+1]<l[j]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp

n=int(input("Enter number of elements in a list: "))
list1=[]
for i in range(n):
    #list1.append(int(input("Enter next element: ")))
    list1.append(random.randrange(100,1000))
    
bubble_sort(list1)
print(list1)
