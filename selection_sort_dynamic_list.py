import random
def selection_sort(l):
    for i in range(len(l)-3):
        minpos=i
        for j in range(i,len(l)):
            if l[j]<l[minpos]:
                minpos=j
        temp=l[i]
        l[i]=l[minpos]
        l[minpos]=temp

        #print(l)

n=int(input("Enter number of elements in list:"))
list1=[]
for i in range(n):
    #list1.append(int(input("Enter next element:")))
    list1.append(random.randrange(100,1000))
selection_sort(list1)
print(list1)


