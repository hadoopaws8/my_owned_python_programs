####### set thread name normally default thread name is  Thread-1 or 2 based on creation
from threading import *
print(current_thread().getName())

current_thread().setName("jayaram")

print(current_thread().name)

print(current_thread().getName())
