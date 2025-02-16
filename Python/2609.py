def LCM(a, b):
    for i in range(min(a, b), 0, -1):
        if a%i == 0 and b%i==0:
            return i

def GCD(a, b):
    lcm = LCM(a, b)
    return int(lcm*(a/lcm)*(b/lcm))

a, b = list(map(int, input().split()))
print(LCM(a, b))
print(GCD(a, b))
