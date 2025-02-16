n = int(input())
scores = list(map(int, input().split()))
best_score = max(scores)
total = 0

for i in range(len(scores)):
    scores[i] = scores[i]/best_score*100
    total += scores[i]

print(total/n)