from collections import deque

n = int(input())
cards = deque(list(map(int, range(1, n+1))))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])