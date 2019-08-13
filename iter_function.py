l=iter([5,2,3,6,8,1])
while True:
    try:
        next_element=next(l)
    except StopIteration as e:
        break
    
    print(next_element)
