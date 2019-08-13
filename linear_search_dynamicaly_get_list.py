pos=-1
def search(li,n1):

    for i in range(len(li)):
        if li[i]==n1:
            globals()['pos']=i
            return True
        
    else:
        return False
    



n=int(input("Enter number of elements you want: "))

list1=[]
for i in range(n):
    list1.append(int(input("enter next element: ")))
print(list1)
find_element=int(input("Enter which element you want to find out: "))

if search(list1,find_element):
    print("your Element found at :",pos+1)
else:
    print("Element not found in list")
