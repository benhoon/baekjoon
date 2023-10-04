import sys

arr = []
N,M = map(int, input().split())

for i in range(N):
  arr += [i+1]
for _ in range(M):
  i,j = map(int, sys.stdin.readline().split())
  for a in range (j,i-1,-1):
    for b in range(i,a,1):
      temp = arr[b-1]
      arr[b-1] = arr[b]
      arr[b] = temp
print(*arr)