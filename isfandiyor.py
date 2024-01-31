from math import pow
n = int(input())
f = pow(n, 5) + 8 * pow(n, 4) - 5 * pow(n, 4) + 3 * pow(n, 2) + n - 12
print(int(f))