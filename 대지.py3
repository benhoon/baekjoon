import sys

N = int(input())
D = []
for i in range(N):
  D.append(list(map(int, sys.stdin.readline().split())))
bottom = D[0][1]
top = D[0][1]
right = D[0][0]
left = D[0][0]

for i in range(N):
  if bottom > D[i][1]:
    bottom = D[i][1]
  if top < D[i][1]:
    top = D[i][1]
  if right < D[i][0]:
    right = D[i][0]
  if left > D[i][0]:
    left = D[i][0]

w = right - left
h = top - bottom

ans = w*h

print(ans)