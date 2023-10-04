import sys
arr = []
for i in range(28):
  n = int(sys.stdin.readline())
  arr += [n]
for i in range(30):
  if i+1 not in arr:
    print(i+1)