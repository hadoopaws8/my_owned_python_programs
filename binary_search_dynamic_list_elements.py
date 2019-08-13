pos=-1
def binary_search(l,n1):
    low=0
    up=len(l)-1
    for i in range(len(l)):
        mid=(low+up)//2
        if l[mid]==n1:
            globals()['pos']=mid
            return True
        else:
            if l[mid]<n1:
                low=mid
            else:
                up=mid
    else:
        return False


n=int(input("Enter the number of elements in list: "))
list1=[]
for i in range(n):
    list1.append(int(input("Enter next element: ")))
find_element=int(input("Enter which element you want to find in list: "))

list1.sort()
print(list1)

if binary_search(list1,find_element):
    print("found at ",pos)
else:
    print("Not found")



