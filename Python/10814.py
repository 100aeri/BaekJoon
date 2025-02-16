n = int(input())
members = []
for i in range(n):
    members.append(input().split())
    members[i][0] = int(members[i][0])

members.sort(key = lambda x: x[0])

for i in range(n):
    print(members[i][0], members[i][1])
