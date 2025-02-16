import sys
_set = set()

input = lambda: sys.stdin.readline().strip()

for _ in range(int(input())):
    command = input().split()
    if len(command) >= 2: x = int(command[1])
    if command[0] == 'add':
        _set.add(x)
    elif command[0] == 'remove':
        _set.discard(x)
    elif command[0] == 'check':
        print(int(x in _set))
    elif command[0] == 'toggle':
        _set.discard(x) if x in _set else _set.add(x)
    elif command[0] == 'all':
        _set = set(list(range(1, 21)))
    elif command[0] == 'empty':
        _set = set()