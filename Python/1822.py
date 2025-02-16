import sys

a, b = list(map(int, sys.stdin.readline().split()))
alist = sorted(list(map(int, sys.stdin.readline().split())))
blist = sorted(list(map(int, sys.stdin.readline().split())))

def binarySearch(k):
    low = 0
    high = b-1
    while high >= low:
        mid = (low+high)//2
        if blist[mid] > k: high = mid - 1
        elif blist[mid] < k: low = mid + 1
        else: return True
    return False

result = []

for i in alist:
    if not binarySearch(i): result.append(i)
print(len(result))
for i in result:
    print(i, end = ' ')
