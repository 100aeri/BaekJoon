from collections import deque

n = int(input())
cards = deque(list(map(int, range(1, n+1))))
trash = deque()

while len(cards) > 1:
    trash.append(cards.popleft())
    cards.append(cards.popleft())

for i in trash:
    print(i, end = ' ')
print(cards[0])