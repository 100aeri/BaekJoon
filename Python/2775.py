import sys

t = int(sys.stdin.readline())
answer = []

for i in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    apt = [[0]*n for _ in range(k+1)]

    apt[0] = list(range(1, n+1))
    for i in range(1, k+1):
        for j in range(n):
            s = 0
            for l in range(j+1): s += apt[i-1][l] # 아래층의 모든 호수 더하기
            apt[i][j] = s
    print(apt[-1][-1])

# memory = {}

# def getResident(k, n):
#     s = 0
#     for i in range(1, n+1):
#         if (k-1, i) not in memory: # 그동안 계산했던 층수를 "기억"한다
#             memory[(k-1, i)] = i if k <= 1 else getResident(k-1, i)
#             # 아래층이 0층인 경우 호수를 저장, 1층 이상인 경우 재귀
#         s += memory[(k-1, i)]
#     return s

# t = int(sys.stdin.readline())
# testcase = [[int(sys.stdin.readline()), int(sys.stdin.readline())] for _ in range(t)]
# for i in testcase:
#     print(getResident(i[0], i[1]))