

##def countsqu(a,b):
##    cnt=0
##    for i in range(a,b+1):
##        j=1
##        while j*j <=i:
##            if j*j ==i:
##                cnt+=1
##                print(j*j)
##                for k in range(j):
##                    if k*k==j:
##                        cnt+=1                
##            j+=1
##        i+=1
##    return cnt
##print(countsqu(10,20))




##count=0
##for i in range(250,261):
##    #print(i)
##    j=1
##    while j*j<=i:
##        if j*j==i:
##            count+=1
##            print(j*j)
##            for k in range(j):
##                if k*k==j:
##                    count+=1
##        j+=1
##print(count)


import math
cnt=0
def sqiroot(n):
    k=int(math.sqrt(n))
    if k==1:
        pass
    else:
        print(k)
        sqiroot(k)
        global cnt
        cnt+=1
    return cnt
p=sqiroot(65536)
print("count: ",p)
            
