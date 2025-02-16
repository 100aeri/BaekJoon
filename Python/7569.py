import sys
import collections

queue = collections.deque()

m, n, h = list(map(int, sys.stdin.readline().split()))
tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

dz = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dx = [0,0,0,0,1,-1]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append((i, j, k, 0))

maxday = 0

while queue:
    z, y, x, day = queue.popleft()
    if maxday < day: maxday = day
    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]
        if (0<= nz <h) and (0<= ny <n) and (0<= nx <m) and (tomato[nz][ny][nx] == 0):
            tomato[nz][ny][nx] = 1
            queue.append((nz, ny, nx, day+1))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                print(-1), quit()

print(maxday)