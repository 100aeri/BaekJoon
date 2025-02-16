import sys

input = lambda: sys.stdin.readline().strip()
print = lambda x : sys.stdout.write('%s\n'%x)

n = int(input())
times = sorted(list(map(int, input().split())))

result = 0
for j in range(n):
    result += times[j]*(n-j)

print(result)