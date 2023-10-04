import sys

arr = [0 for i in range(9)]
max = 0

for i in range(9):
  arr[i] = list(map(int, sys.stdin.readline().split()))

for i in arr:
  for j in i:
    if j > max:
      max = j

for i in range(9):
  for j in range(9):
    if max == arr[i][j]:
      col = i
      row = j
print(max)
print(col+1, row+1)