n = input()
list = list(map(int, input().split()))
count = 0

def check_deci(num):
    if num == 1: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

for i in list:
    if check_deci(i): count += 1

print (count)