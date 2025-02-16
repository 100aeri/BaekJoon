n, k = list(map(int, input().split()))
l = list(range(1, n+1))
res = []
cnt1 = 0
cnt2 = 1

while l:
    if cnt1 >= len(l): cnt1 = 0
    if cnt2 >= k:
        res.append(l.pop(cnt1))
        cnt2 = 0
        cnt1 -= 1
    cnt1 += 1
    cnt2 += 1
    
print('<'+str(res)[1:-1]+'>')