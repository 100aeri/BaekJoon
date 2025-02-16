import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))
card_dict = {}

for i in cards:
    if i in card_dict: card_dict[i] += 1
    else: card_dict[i] = 1

for i in find:
    print(card_dict[i], end = ' ') if i in card_dict else print(0, end = ' ')


