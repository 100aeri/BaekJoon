import sys
import collections

queue = collections.deque()

m, n= list(map(int, sys.stdin.readline().split()))
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dy = [1,-1,0,0]
dx = [0,0,1,-1]

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i, j, 0))

maxday = 0

while queue:
    y, x, day = queue.popleft()
    if maxday < day: maxday = day
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0<= ny <n) and (0<= nx <m) and (tomato[ny][nx] == 0):
            tomato[ny][nx] = 1
            queue.append((ny, nx, day+1))

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1), quit()

print(maxday)