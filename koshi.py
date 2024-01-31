from math import sqrt 
a = int(input("a = "))
b = int(input("b = "))
if (a + b) / 2 > sqrt(a * b):
    print(">")
elif (a + b) / 2 < sqrt(a * b):
    print("<")
elif (a + b) / 2 == sqrt(a * b):
    print("=")