import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
no_hear = {input().strip() for _ in range(n)}
no_see = {input().strip() for _ in range(m)}
no_hear_see = sorted(no_hear&no_see)

print(len(no_hear_see))
for i in no_hear_see:
    print(i)