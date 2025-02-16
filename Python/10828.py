n = int(input())
command = []
stack = []

def push(data):
    stack.append(data)

def pop():
    if not empty(): return stack.pop()
    else: return -1

def size():
    return len(stack)

def empty():
    return (size() == 0)

def top():
    if not empty(): return stack[-1]
    else: return -1

for i in range(n):
    command.append(input())
for i in command:
    if "push" in i:
        data = int(list(i.split())[1])
        push(data)
    elif "pop" in i:
        print(pop())
    elif "size" in i:
        print(size())
    elif "empty" in i:
        print(int(empty()))
    elif "top" in i: 
        print(top())