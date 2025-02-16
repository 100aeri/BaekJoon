i = 0

while True:
    if list(map(int, input().split()))[0] == 0: break
    else:
        i += 1

for j in range(i):
    print('Case %s: Sorting... done!'%(j+1))
    