def palindrome(n):
    num_list = [int(i) for i in str(n)]
    for i in range(len(num_list)//2):
        if num_list[i] != num_list[len(num_list)-i-1]: return False
    return True

n = -1
while n != 0:
    n = int(input())
    if n == 0: break
    print('yes' if palindrome(n) else 'no')