n, k = list(map(int, input().split()))
n_fac = k_fac = 1
for i in range(n-k):
    n_fac = n_fac * (n-i)
    k_fac = k_fac * (i+1)
print(int(n_fac/k_fac))