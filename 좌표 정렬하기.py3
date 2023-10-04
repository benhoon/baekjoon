import sys

N = int(input())
p = [[0] for i in range(N)]

for i in range(N):
  p[i] = list(map(int, sys.stdin.readline().split()))

p.sort()

for i in range(N):
  print(*p[i])