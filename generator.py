def sample(a,b,c):
    add=a+b
    print("before yield")
    yield add
    print("after yield of add")
    sub=b-a
    print("before yield of sub")
    yield sub
    print("after yield of sub")
    mul=a*c
    print("before yield of mul")
    yield mul
    print("after yield of mul")

p=sample(2,3,6)
print(p)
print(next(p))
print(next(p))
print(next(p))
print(next(p))
#print(next(p))
