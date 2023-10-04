import sys

arr = []
result = 1

for i in range(10):    #숫자 10개 입력
  n = int(sys.stdin.readline())
  arr += [n%42]

arr.sort()

for i in range(9):
  if arr[i] != arr[i+1]:
    result = result + 1
print(result)