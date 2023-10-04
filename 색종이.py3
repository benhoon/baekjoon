import sys

N = int(input())
pp= [[0]*100 for i in range(100)]
ans = 0
for i in range(N):
  X,Y = map(int, sys.stdin.readline().split())
  for j in range(Y-1, Y+9, 1):
    for _ in range(X-1, X+9, 1):
      pp[j][_] = 1
for i in pp:
  ans += i.count(1)
  
print(ans)