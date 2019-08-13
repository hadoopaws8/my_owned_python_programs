def fib(mymax):
    a,b=0,1
    while True:
        c=a+b
        if c < mymax:
            print("before yield function")
            yield c
            print("after yield function")
            a=b
            b=c
        else:
            break
gen=fib(10)
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
#print(next(gen)) # it will error for StopIteration
