##try:
##    print("strat")
##    #1/0
##    #c=abc
##    print("Hello World")
##except Exception as e:
##    print(e)
##    print(type(e))


##try:
##    print("strat")
##    #1/0
##    c=abc
##    print("Hello World")
##except ZeroDivisionError as e:
##    print(e)
##    print(type(e))
##except Exception as e:    # Exception keyword has handle all type of errors
##    print(e)
##finally:
##    print("Bye")


##try:
##    print("strat")
##    1/0
##except ZeroDivisionError as e:
##    print(e)
##try:    
##    c=abc
##    print("Hello World")
##except Exception as e:
##    print(e)
##    print(type(e))
##finally:
##    print("Bye")

l=iter([5,2,3,6,8,1])
while True:
    try:
        next_element=next(l)
    except StopIteration as e:
        break
    print(next_element)




