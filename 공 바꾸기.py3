import sys

N, M = map(int, input().split())

arr = []

for i in range(N): #바구니 번호대로 공
  arr += [i+1]

for _ in range(M):
  i,j = map(int, sys.stdin.readline().split())
  
  temp = arr[i-1]
  arr[i-1] = arr[j-1]
  arr[j-1] = temp
print(*arr)