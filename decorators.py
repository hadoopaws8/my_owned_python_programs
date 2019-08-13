def upper_d(func):
    def inner():
        str1 = func()
        print(str1)
        return str1.upper()
    return inner
def split_d(func):
    def wrapper():
        str2 = func()
        print(str2)
        return str2.split()
    return wrapper

@split_d              # Here first upper_d and then split_d is working 
@upper_d
def ordinary():
    return "good morning"
print(ordinary())
