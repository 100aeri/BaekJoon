n = int(input())
list = []

def isVPS(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0 or stack[len(stack)-1] != "(":
                return False
            stack.pop()
    return (len(stack) == 0)

for i in range(n):
    list.append(input())
for i in list:
    if(isVPS(i)): print("YES")
    else: print("NO")