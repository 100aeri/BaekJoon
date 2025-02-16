queue = []
front = 0
rear = -1
command = []

n = int(input())

for i in range(n):
    command.append(input())

for i in command:
    if "push" in i:
        data = int(list(i.split())[1])
        queue.append(data)
        rear += 1

    elif "pop" in i:
        if len(queue) > 0:
            print(queue[front])
            front += 1
            for i in range(front,rear+1):
                queue[i-1] = queue[i]
            front -= 1
            queue.pop()
            rear -= 1
        else: print(-1)

    elif "size" in i:
        print(len(queue))

    elif "empty" in i:
        print(int(len(queue) == 0))

    elif "front" in i: 
        if len(queue) > 0: print(queue[front])
        else: print(-1)

    elif "back" in i: 
        if len(queue) > 0: print(queue[rear])
        else: print(-1)
