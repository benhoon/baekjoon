import sys

N = int(input())
p = [[0] for i in range(N)]

for i in range(N):
  p[i] = list(map(int, sys.stdin.readline().split()))

for i in range(N):
  temp = p[i][0]
  p[i][0] = p[i][1]
  p[i][1] = temp
p.sort()

for i in range(N):
  temp = p[i][0]
  p[i][0] = p[i][1]
  p[i][1] = temp

for i in range(N):
  print(*p[i])