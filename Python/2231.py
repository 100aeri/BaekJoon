import sys
from math import log10

input = sys.stdin.readline

n = int(input())
g = 0

if n == 1:
    print(0)
    exit()

for i in range(int(log10(n)-1), n):
    if i + sum(list(map(int, str(i)))) == n:
        print(i)
        exit()
print(0)