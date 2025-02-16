import sys

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]

def merge(a, b):
    res = []
    ia = ib = 0
    while ia < len(a) and ib < len(b):
        if a[ia] <= b[ib]:
            res.append(a[ia])
            ia += 1
        else:
            res.append(b[ib])
            ib += 1
    if ia == len(a): res += b[ib:]
    else: res += a[ia:]
    return res

def mergeSort(list):
    if len(list) <= 1: return list

    middle = len(list)//2
    left = mergeSort(list[:middle])
    right = mergeSort(list[middle:])
    return merge(left, right)

res = mergeSort(numbers)
for i in res:
    print(i)


