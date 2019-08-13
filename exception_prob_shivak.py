##def functionName(level):
##    if level<1:
##        raise Exception(level)
##    return level
##try:
##    l=functionName(5)
##    print("level=",l)
##except Exception as e:
##    print("Error in level arguments",e.args[0])

l=[1,2,3,4]
def errorHand(val):
    if val not in l:
        raise Exception(val)
    return val

try:
    n=int(input("choose the vaule what i am enter here 1,2,3,4: "))
    if l[0]==n:
        print("addition")
    elif l[1]==n:
        print("subraction")
    elif l[2]==n:
        print("multiplication")
    elif l[3]==n:
        print("division")
    else:
        errorHand(n)
except ValueError as e:
    print("alphabes and sysmbols are not suport")
except Exception as e:
    print("element",e,"Not in list ")


##class Error(Exception):
##    pass
##class ValueTooSmallError(Error):
##    pass
##class ValueTooLargeError(Error):
##    pass
##def main():
##    number=10
##    try:
##        i_num=int(input("please enter an integer:"))
##
##        if i_num<number:
##            raise ValueTooSmallError
##        if i_num >number:
##            raise ValueTooLargeError
##        else:
##            print("perfect!")
##    except ValueTooSmallError:
##        print("The value is too small")
##    except ValueTooLargeError:
##        print("The value is too large")
##    except Exception:
##        print("Unexpected error")
##if __name__=="__main__":
##    main()



