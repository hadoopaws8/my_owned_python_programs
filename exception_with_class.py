##class B(Exception):
##    pass
##class C(B):
##    pass
##class D(C):
##    pass
##for cls in [B,C,D]:
##    try:
##        print(cls)
##        raise cls()
##    except D:
##        print("D")
##    except C:
##        print("C")
##    except B:
##        print("B")


import sys
try:
    f=open(r'C:\Users\jaya\Desktop\calculater\jaya.txt','r')
    s=f.readline()
    i=int(s.strip())
except OSError as e:
    print("OS error :{0}",format(e))
except ValueError :
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:",sys.exc_info()[0])
    raise
