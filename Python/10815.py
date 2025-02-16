import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
m = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))

def binarySearch(k):
    low = 0
    high = n-1
    while high >= low:
        mid = (low+high)//2
        if cards[mid] > k: high = mid - 1
        elif cards[mid] < k: low = mid + 1
        else: return True
    return False

for i in find:
    print(1, end = ' ') if binarySearch(i) else print(0, end = ' ')
