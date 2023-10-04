import sys

N = int(input())
list_n = []

for i in range(N):
  list_n.append(int(sys.stdin.readline()))
list_n.sort()

for i in range(N):
  print(list_n[i])