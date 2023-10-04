import sys

N = int(input())
mem = []

for i in range(N):
  mem.append(list(map(str, sys.stdin.readline().rstrip().split())))
for i in range(N):
  mem[i][0] = int(mem[i][0])

mem.sort(key=lambda x:x[0])

for i in mem:
  print(*i)