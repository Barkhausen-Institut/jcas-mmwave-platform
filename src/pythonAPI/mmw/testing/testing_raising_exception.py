"""Testing exceptions"""

import sys

def increment(a):
    if a < 10:
        raise Exception("Too low value: %s"%str(a))
    return a+1

def add(a,b):
    a = increment(a)
    if a<b:
        raise Exception("Invalid parameters")
    return a+b

try:
    print(add(2,3))
except:
    print(sys.exc_info()[1])


# a: list
a = ["", "1"]
print(type(a))
if isinstance(a, list): print("'a' is a list")
