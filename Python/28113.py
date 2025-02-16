n, a, b = list(map(int, input().split()))
if a < b:
    print('Bus')
elif a == b: print('Anything')
else:
    print('Subway')