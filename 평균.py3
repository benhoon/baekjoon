import sys

n = int(input())
score = list(map(int, input().split()))
M = 0
sum = 0

for _ in range(n):
  if score[_]>M:
    M = score[_]
for _ in range(n):
  score[_] = score[_]/M*100
for _ in range(n):
  sum = sum + score[_]
avg = sum / n

print(avg)