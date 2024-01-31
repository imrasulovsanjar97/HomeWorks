from math import sqrt 
a = int(input("a = ")) 
b = int(input("b = "))
if sqrt(a + b) > sqrt(a * b):
    print(">")
elif sqrt(a + b) < sqrt(a * b):
    print("<")
elif sqrt(a + b) == sqrt(a * b):
    print("=")