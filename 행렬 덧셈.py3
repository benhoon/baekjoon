import sys

N,M = map(int, input().split())
arr1 = [0 for _ in range(N)]
arr2 = [0 for _ in range(N)]
sum = [[0 for _ in range(M)] for i in range(N)]

for i in range(N):
  arr1[i] = list(map(int, sys.stdin.readline().split()))
for i in range(N):
  arr2[i] = list(map(int, sys.stdin.readline().split()))

for i in range(N):
  for j in range(M):
    sum[i][j] = arr1[i][j] + arr2[i][j]
for i in sum:
  for j in i:
    print(j, end = ' ')
  print("")