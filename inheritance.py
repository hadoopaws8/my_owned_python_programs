            #single inheritance#
##class A:
##    def __init__(self):
##        print('hellow  A')
##    def sample(self):
##        print("Hi jayaram   A")
##class B(A):
##    def __init__(self):
##        super().__init__()
##        #super().__init__()
##        print('this is B')
##    def sample(self):
##        super().sample()
##        print("fun B")
##p=B()
##p.sample()


##class A:
##    def __init__(self):
##        print('Initializing: class A')
##
##    # def sub_method(self, b):
##    #     print('Printing from class A:', b)
##
##class B(A):
##    def __init__(self):
##        print('Initializing: class B')
##        super().__init__()
##
##    # def sub_method(self, b):
##    #     print('Printing from class B:', b)
##    #     super().sub_method(b + 1)
##c = B()
### c.sub_method(1)

            # multiple inheritance
            #here first which class is taken that will display (MRO-method resolution order)

##class A:
##    def __init__(self,name):
##        print("This is A __init__")
##        self.nm=name
##    def sam(self):
##        print("This is A function name :",self.nm)
##    
##class B:
##    def __init__(self,name):
##        self.nm=name
##        print("This is B __init__")
##    def sam(self):
##        print("This is B function name :",self.nm)
##class C(B,A):
##    def __init__(self,name):
##        self.nm=name
##        super().__init__(name)
##        print("This is C __init__")
##    def sam(self):
##        super().sam()
##        print("This is C function name :",self.nm)
##
##c = C("jaya")
##c.sam()
##


                    ### INNER class

class stu:
    def __init__(self,name,roll):
        self.nm=name
        self.rn=roll
        self.lap=self.laptop
    def show(self):
        print(self.nm,self.rn)
    class laptop:
        def __init__(self):
            self.brand="HP"
            self.ram=8
s=stu("jaya",2)
s.show()
##lap=stu.laptop()
##print(lap.brand)
##print(lap.ram)

lap=s.lap()
print(lap.ram)

    



