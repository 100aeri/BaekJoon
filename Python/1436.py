import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
ans = 666
while True:
    if '666' in str(ans):
        n -= 1
    if n <= 0:
        print(ans)
        break
    ans += 1