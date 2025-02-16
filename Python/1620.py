import sys

pokedex = dict()
rev_pokedex = dict()
input = lambda: sys.stdin.readline().strip()
print = lambda x: sys.stdout.write('%s\n'%x)

n, m = map(int, input().split())

for i in range(1, n+1):
    name = input()
    pokedex[i] = name
    rev_pokedex[name] = i

for _ in range(m):
    question = input()
    if question.isdigit():
        print(pokedex[int(question)])
    else:
        print(rev_pokedex[question])