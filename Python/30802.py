import sys

n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

tshirt = 0
for i in size:
    while (i > 0):
        i = i - t
        tshirt += 1

print("%s\n%s %s"%(tshirt, n//p, n%p))
