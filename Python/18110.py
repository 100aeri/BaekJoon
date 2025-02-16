n = int(input())

if n == 0:
    print(0)
else:
    vote = []
    result = 0
    excp = int(n*0.15+0.5) #제외할 사람 수
    for i in range(n):
        vote.append(int(input()))
    vote.sort()
    vote = vote[excp:n-excp]
    for i in vote: result += i
    print(int(result / (n - excp*2) + 0.5))