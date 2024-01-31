n = int(input("n = "))
a = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
s = 0
while n > 0:
    b = n % 10
    s += a[b]
    n = n // 10
print(s)
    